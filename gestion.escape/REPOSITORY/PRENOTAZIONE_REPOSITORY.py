import json
from MODELS.PRENOTAZIONE import Prenotazione


class PrenotazioneRepository:

    def __init__(self, path: str = "prenotazioni.json"):
        self._path = path
        self._prenotazioni: dict = {}
        self.carica()

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                dati = json.load(f)
            self._prenotazioni = {
                d["idPrenotazione"]: Prenotazione.fromDict(d) for d in dati
            }
        except FileNotFoundError:
            self._prenotazioni = {}

    def salva(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump([p.toDict() for p in self._prenotazioni.values()],
                      f, indent=2, ensure_ascii=False)

    def trovaPerId(self, idPrenotazione: str) -> Prenotazione:
        return self._prenotazioni[idPrenotazione]

    def trovaPerCliente(self, idCliente: str) -> list:
        """Restituisce le prenotazioni confermate e non disdette del cliente."""
        return [p for p in self._prenotazioni.values()
                if p.getIdCliente() == idCliente
                and p.getStatoPrenotazione() is True
                and p.getStatoDisdetta() is False]

    def trovaAttivePerStanzaEGiorno(self, idStanza: str, giorno: str) -> list:
        return [p for p in self._prenotazioni.values()
                if (p.getIdStanza() == idStanza
                    and p.getGiorno() == giorno
                    and p.getStatoPrenotazione() is True
                    and p.getStatoDisdetta() is False)]

    def aggiungi(self, prenotazione: Prenotazione) -> None:
        self._prenotazioni[prenotazione.getIdPrenotazione()] = prenotazione
        self.salva()

    def aggiorna(self, prenotazione: Prenotazione) -> None:
        self._prenotazioni[prenotazione.getIdPrenotazione()] = prenotazione
        self.salva()

    def tutti(self) -> list:
        return list(self._prenotazioni.values())
