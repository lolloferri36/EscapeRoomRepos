class Utente:
    
    def __init__(self, email: str, password: str, statoAccesso: bool = False):
        self._email = email
        self._password = password
        self._statoAccesso = statoAccesso

    def getEmail(self) -> str:
        return self._email

    def getPassword(self) -> str:
        return self._password

    def getStatoAccesso(self) -> bool:
        return self._statoAccesso

    def setStatoAccesso(self, eseguito: bool) -> None:
        if not isinstance(eseguito, bool):
            raise TypeError("Lo stato di accesso deve essere un valore booleano.")
        self._statoAccesso = eseguito

    def toDict(self) -> dict:
        return {
            "email": self._email,
            "password": self._password,
            "statoAccesso": self._statoAccesso
        }

    @classmethod
    def fromDict(cls, data: dict) -> 'Utente':
        return cls(data["email"], data["password"], data["statoAccesso"]) 

    def __str__(self) -> str:
        set = "Accesso Eseguito" if self._statoAccesso else "Accesso non eseguito"
        return f"Email: {self._email} [{set}]"

