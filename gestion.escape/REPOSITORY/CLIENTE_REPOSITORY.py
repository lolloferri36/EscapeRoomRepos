import json
from MODELS.CLIENTE import Cliente


class ClienteRepository:

    def __init__(self, path: str = "clienti.json"):
        self._path = path
        self._clienti: dict = {} 
        self.carica()

    def carica(self) -> None:
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                dati = json.load(f)
            self._clienti = {d["idCliente"]: Cliente.fromDict(d) for d in dati}
        except FileNotFoundError:
            self._clienti = {}

    def salva(self) -> None:
        with open(self._path, "w", encoding="utf-8") as f:
            json.dump([c.toDict() for c in self._clienti.values()],
                      f, indent=2, ensure_ascii=False)

    def trovaPerId(self, idCliente: str) -> Cliente:
        return self._clienti[idCliente]

    def trovaPerEmail(self, email: str) -> Cliente | str:
        for cliente in self._clienti.values():
            if cliente.getEmail() == email:
                return cliente
        return "Email non trovata"

    def trovaPerEmailEPassword(self, email: str, password: str) -> Cliente | str:

        for cliente in self._clienti.values():
            if cliente.getEmail() == email and cliente.getPassword() == password:
                return cliente
        return "Email o password errati"

    def aggiungi(self, cliente: Cliente) -> None:
        self._clienti[cliente.getIdCliente()] = cliente
        self.salva()

    def tutti(self) -> list:
        return list(self._clienti.values())
