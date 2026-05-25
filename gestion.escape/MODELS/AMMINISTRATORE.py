from MODELS.UTENTE import Utente


class Amministratore(Utente):

    def __init__(self, idAdmin: str, email: str, password: str,
                 statoAccesso: bool = False):
        super().__init__(email, password, statoAccesso)
        self._idAdmin = idAdmin

    def getIdAdmin(self) -> str:
        return self._idAdmin

    def toDict(self) -> dict:
        data = super().toDict()
        data["idAdmin"] = self._idAdmin
        return data

    @classmethod
    def fromDict(cls, data: dict) -> "Amministratore":
        return cls(
            data["idAdmin"],
            data["email"],
            data["password"],
            data["statoAccesso"]
        )

    def __str__(self) -> str:
        info_amministratore = super().__str__()  
        return f"{self._idAdmin}-{info_amministratore}"
