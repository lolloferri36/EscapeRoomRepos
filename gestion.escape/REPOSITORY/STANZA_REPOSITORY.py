import json
from MODELS.STANZA import Stanza

class StanzaRepository:

    def __init__(self, path: str="stanze.json"):
        self._path = path
        self._stanze: dict = {}    
        self.carica()

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                dati = json.load(f)
            self._stanze = {d["idStanza"]: Stanza.fromDict(d) for d in dati}
        except FileNotFoundError:
            self._stanze = {}

    def salva(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump([s.toDict() for s in self._stanze.values()],
                      f, indent=2, ensure_ascii=False)

    def trovaPerId(self, idStanza: str) -> Stanza:
        return self._stanze[idStanza]

    def aggiungi(self, stanza: Stanza) -> None:
        self._stanze[stanza.getIdStanza()] = stanza
        self.salva()

    def tutti(self) -> list:
        return list(self._stanze.values())
