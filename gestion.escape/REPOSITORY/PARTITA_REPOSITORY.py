import json
from MODELS.PARTITA import Partita


class PartitaRepository:

    def __init__(self, path: str = "partite.json"):
        self._path = path
        self._partite: dict = {}
        self.carica()

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                dati = json.load(f)
            self._partite = {d["idPartita"]: Partita.fromDict(d) for d in dati}
        except FileNotFoundError:
            self._partite = {}

    def salva(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump([p.toDict() for p in self._partite.values()],
                      f, indent=2, ensure_ascii=False)

    def trovaPerId(self, idPartita: str) -> Partita:
        return self._partite[idPartita]

    def aggiungi(self, partita: Partita) -> None:
        self._partite[partita.getIdPartita()] = partita
        self.salva()

    def aggiorna(self, partita: Partita) -> None:
        self._partite[partita.getIdPartita()] = partita
        self.salva()

    def trovaStoricoPerCliente(self, idCliente: str) -> list:
        return [p for p in self._partite.values()
                if p.getIdCliente() == idCliente and p.getEsito() is not None]

    def tutti(self) -> list:
        return list(self._partite.values())
