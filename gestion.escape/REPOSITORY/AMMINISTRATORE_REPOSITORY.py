import json
from MODELS.AMMINISTRATORE import Amministratore

class AmministratoreRepository:
   
    def __init__(self, path: str = "amministratore.json"):
        self._path = path
        self._admin: Amministratore = None
        self.carica()

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if data:
                self._admin = Amministratore.fromDict(data)
        except FileNotFoundError:
            self._admin = None

    def getAdmin(self) -> Amministratore:
        return self._admin

    def verificaCredenziali(self, email: str, password: str) -> bool:
        
        if self._admin is None:
            return False
        return (self._admin.getEmail() == email and
                self._admin.getPassword() == password)
