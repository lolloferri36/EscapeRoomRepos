from REPOSITORY.CLIENTE_REPOSITORY import ClienteRepository

class GestoreCliente:

    def __init__(self, cliente_repo: ClienteRepository):
        self._cliente_repo = cliente_repo

    def elencaClienti(self) -> list:
        return self._cliente_repo.tutti()
