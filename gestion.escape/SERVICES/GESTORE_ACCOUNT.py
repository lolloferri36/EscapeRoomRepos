import uuid
from typing import Tuple
from REPOSITORY.AMMINISTRATORE_REPOSITORY import AmministratoreRepository
from REPOSITORY.CLIENTE_REPOSITORY import ClienteRepository
from MODELS.CLIENTE import Cliente
from MODELS.AMMINISTRATORE import Amministratore


class GestoreAccount:

    def __init__(self, amministratore_repo: AmministratoreRepository,
                 cliente_repo: ClienteRepository):
        self._amministratore_repo = amministratore_repo
        self._cliente_repo = cliente_repo

    def registrazione(self, email: str, password: str) -> str:
        if not email.strip() or not password.strip():
           return "Errore: email e password non possono essere vuoti"
        
        risultato = self._cliente_repo.trovaPerEmail(email)
        if isinstance(risultato, Cliente):
            return f"Errore: l'email '{email}' è già in uso."
        nuovo_cliente = Cliente(str(uuid.uuid4()), email, password)
        self._cliente_repo.aggiungi(nuovo_cliente)
        return "Registrazione avvenuta con successo. Puoi ora effettuare l'accesso."

    def accessoCliente(self, email: str, password: str) -> Tuple[Cliente, str]:
        cliente = self._cliente_repo.trovaPerEmailEPassword(email, password)
        if not isinstance(cliente, Cliente):
            return None, "Errore: credenziali non valide"
        cliente.setStatoAccesso(True)
        return cliente, f"Benvenuto, {cliente.getEmail()}!"

    def accessoAmministratore(self, email: str, password: str) -> Tuple[Amministratore, str]:
        if not self._amministratore_repo.verificaCredenziali(email, password):
            return None, "Errore: credenziali amministratore non valide"
        amministratore = self._amministratore_repo.getAdmin()
        amministratore.setStatoAccesso(True)
        return amministratore, f"Benvenuto, Amministratore {amministratore.getEmail()}!"
