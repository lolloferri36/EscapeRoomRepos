from datetime import datetime


class Partita:
    DURATA_MASSIMA = 90

    def __init__(self, idPartita: str, idCliente: str, idPrenotazione: str,
                 esito: str = None, tempoInizio: datetime = None, tempoFine: datetime = None):
        self._idPartita = idPartita
        self._idCliente = idCliente
        self._idPrenotazione = idPrenotazione
        self._esito: str = esito 
        self._tempoInizio: datetime = tempoInizio
        self._tempoFine: datetime = tempoFine
        self._indiceSuggerimento: int = 0
 
    def avvia(self) -> None:
        self._tempoInizio = datetime.now()

    def termina(self) -> str:
        if self._tempoInizio is None:
            return "La partita non è ancora cominciata"
        self._tempoFine = datetime.now()
        minuti = (self._tempoFine - self._tempoInizio).total_seconds() / 60
        self._esito = "vittoria" if minuti <= self.DURATA_MASSIMA else "sconfitta"
        return self._esito

    def abbandona(self) -> str:
        if self._tempoInizio is None:
            return "La partita non è ancora cominciata"
        self._tempoFine = datetime.now()
        self._esito = "sconfitta"
        return self._esito

    def chiediSuggerimento(self, suggerimenti: list) -> str:
        if not suggerimenti:
            return "Nessun suggerimento disponibile per questa stanza."
        if self._indiceSuggerimento >= len(suggerimenti):
            return "Hai già ricevuto tutti i suggerimenti disponibili per questa stanza."
        hint = suggerimenti[self._indiceSuggerimento]
        self._indiceSuggerimento += 1
        rimasti = len(suggerimenti) - self._indiceSuggerimento
        return (f"💡 Suggerimento {self._indiceSuggerimento}/{len(suggerimenti)}: {hint}\n"
                f"   (Suggerimenti rimanenti: {rimasti})")

    def getIdPartita(self) -> str:
        return self._idPartita

    def getIdCliente(self) -> str:
        return self._idCliente

    def getIdPrenotazione(self) -> str:
        return self._idPrenotazione

    def getEsito(self) -> str:
        return self._esito

    def isAvviata(self) -> bool:
        return self._tempoInizio is not None and self._tempoFine is None

    def toDict(self) -> dict:
        return {
            "idPartita": self._idPartita,
            "idCliente": self._idCliente,
            "idPrenotazione": self._idPrenotazione,
            "esito": self._esito,
            "tempoInizio": self._tempoInizio.isoformat() if self._tempoInizio else None,
            "tempoFine": self._tempoFine.isoformat() if self._tempoFine else None,
        }

    @classmethod
    def fromDict(cls, d: dict) -> "Partita":
        return cls(
            d["idPartita"],
            d["idCliente"],
            d["idPrenotazione"],
            d.get("esito"),
            d.get("tempoInizio"),
            d.get("tempoFine"),
        )

    def __str__(self) -> str:
        if self._tempoInizio and self._tempoFine:
            minuti = (self._tempoFine - self._tempoInizio).total_seconds() / 60
        else:
            minuti = 0.0
        esito = self._esito or "in corso"
        return f"[{self._idPartita}] — {minuti:.1f} min — {esito}"     
