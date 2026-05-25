class Stanza:

    def __init__(self, idStanza: str, descrizione: str, prezzo: float,
                 nome: str, tipo: str, stato: bool = True, suggerimenti: list = None):
        self._idStanza = idStanza
        self._descrizione = descrizione
        self._prezzo = prezzo       
        self._nome = nome
        self._tipo = tipo   #True intende libera, altrimenti occupata
        self._stato = stato         
        self._suggerimenti = suggerimenti if suggerimenti is not None else []

    def getIdStanza(self) -> str:
        return self._idStanza

    def getDescrizione(self) -> str:
        return self._descrizione

    def getPrezzo(self) -> float:
        return self._prezzo

    def getNome(self) -> str:
        return self._nome

    def getTipo(self) -> str:
        return self._tipo

    def isDisponibile(self) -> bool:
        return self._stato

    def getSuggerimenti(self) -> list:
        return self._suggerimenti

    def setStato(self, stato: bool) -> None:
        if not isinstance(stato, bool):
            raise TypeError("Il valore deve essere un booleano ") 
        self._stato = stato

    def setDatiStanze(self, nome: str, tipo: str, descrizione: str) -> None:
        if not isinstance(nome, str) or not isinstance(tipo, str) or not isinstance(descrizione, str):
            raise TypeError("nome, tipo e descrizione devono essere delle stringhe")
        self._nome = nome
        self._tipo = tipo
        self._descrizione = descrizione

    def toDict(self) -> dict:
        return {
            "idStanza": self._idStanza,
            "descrizione": self._descrizione,
            "prezzo": self._prezzo,
            "nome": self._nome,
            "tipo": self._tipo,
            "stato": self._stato,
            "suggerimenti": self._suggerimenti
        }

    @classmethod
    def fromDict(cls, d: dict) -> "Stanza":
        return cls(d["idStanza"], d["descrizione"], d["prezzo"],
                   d["nome"], d["tipo"], d["stato"],
                   d.get("suggerimenti", []))

    def __str__(self) -> str:
        return f"[{self._idStanza}] {self._nome} [{self._tipo}]:{self._descrizione} ---- {self._prezzo}€"
