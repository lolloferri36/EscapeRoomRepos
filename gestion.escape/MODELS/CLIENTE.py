from MODELS.UTENTE import Utente


class Cliente(Utente):

    def __init__(self, idCliente: str, email: str, password: str, statoAccesso: bool = False):
        super().__init__(email, password, statoAccesso)
        self._idCliente = idCliente 

    def getIdCliente(self) -> str:
        return self._idCliente

    def toDict(self) -> dict:
        data = super().toDict()
        data["idCliente"] = self._idCliente
        return data

    @classmethod
    def fromDict(cls, data: dict) -> "Cliente":
        return cls(
            data["idCliente"],
            data["email"],
            data["password"],
            data["statoAccesso"],
        )

    def __str__(self) -> str:
        info_cliente = super().__str__()
        return f"[{self._idCliente}]-{info_cliente}"
