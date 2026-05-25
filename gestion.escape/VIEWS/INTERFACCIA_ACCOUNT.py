from SERVICES.GESTORE_ACCOUNT import GestoreAccount
from MODELS.CLIENTE import Cliente
from MODELS.AMMINISTRATORE import Amministratore


class InterfacciaAccount:

    def __init__(self, gestore: GestoreAccount):
        self._gestore = gestore

    def registra(self) -> None:

        print("\n--- REGISTRAZIONE ---")
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        esito = self._gestore.registrazione(email, password)
        print(f"\n→ {esito}")

    def accediCliente(self) -> Cliente:
        
        print("\n--- ACCESSO CLIENTE ---")
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        cliente, msg = self._gestore.accessoCliente(email, password)
        print(f"\n→ {msg}")
        return cliente

    def accediAmministratore(self) -> Amministratore:

        print("\n--- ACCESSO AMMINISTRATORE ---")
        email = input("Email: ").strip()
        password = input("Password: ").strip()
        amministratore, msg = self._gestore.accessoAmministratore(email, password)
        print(f"\n→ {msg}")
        return amministratore
