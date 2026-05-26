class Prenotazione:

    def __init__(self, idPrenotazione: str, idCliente: str, idStanza: str,
                 statoPrenotazione: bool = False,
                 giorno: str = None, ora: str = None,
                 statoDisdetta: bool = False):
        self._idPrenotazione = idPrenotazione
        self._idCliente = idCliente
        self._idStanza = idStanza
        self._giorno = giorno
        self._ora = ora
        self._statoPrenotazione = statoPrenotazione
        self._statoDisdetta = statoDisdetta

    def getIdPrenotazione(self) -> str:
        return self._idPrenotazione

    def getIdCliente(self) -> str:
        return self._idCliente

    def getIdStanza(self) -> str:
        return self._idStanza

    def getGiorno(self) -> str:
        return self._giorno

    def getOra(self) -> str:
        return self._ora

    def getGiornoOra(self) -> tuple:
        return self._giorno, self._ora

    def getStatoPrenotazione(self) -> bool:
        return self._statoPrenotazione

    def getStatoDisdetta(self) -> bool:
        return self._statoDisdetta

    def setStatoPrenotazione(self, statoPrenotazione: bool) -> None:
        if not isinstance(statoPrenotazione, bool):
            raise TypeError("Lo stato della prenotazione deve essere un valore booleano")
        self._statoPrenotazione = statoPrenotazione

    def setStatoDisdetta(self, statoDisdetta: bool) -> None:
        if not isinstance(statoDisdetta, bool):
            raise TypeError("Lo stato della disdetta deve essere un valore booleano")
        self._statoDisdetta = statoDisdetta

    def setGiornoOra(self, giorno: str, ora: str) -> None:
        self._giorno = giorno
        self._ora = ora

    def toDict(self) -> dict:
        return {
            "idPrenotazione": self._idPrenotazione,
            "idCliente": self._idCliente,
            "idStanza": self._idStanza,
            "giorno": self._giorno,
            "ora": self._ora,
            "statoPrenotazione": self._statoPrenotazione,
            "statoDisdetta": self._statoDisdetta,
        }

    @classmethod
    def fromDict(cls, d: dict) -> "Prenotazione":
        return cls(
            d["idPrenotazione"],
            d["idCliente"],
            d["idStanza"],
            d["statoPrenotazione"],
            d.get("giorno"),
            d.get("ora"),
            d["statoDisdetta"],
        )

    def __str__(self) -> str:
        stato = "confermata" if self._statoPrenotazione else "non confermata"
        disdetta = "disdetta" if self._statoDisdetta else "non disdetta"
        return f"[{self._idPrenotazione}] — {self._giorno} {self._ora} — {stato} ({disdetta})"
