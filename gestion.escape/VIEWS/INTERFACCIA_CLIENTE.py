from SERVICES.GESTORE_CLIENTE import GestoreCliente


class InterfacciaCliente:

    def __init__(self, gestore: GestoreCliente):
        self._gestore = gestore

    def mostraClienti(self) -> None:

        print("\n--- CLIENTI REGISTRATI ---")
        clienti = self._gestore.elencaClienti()
        if not clienti:
            print("Nessun cliente registrato.")
            return
        print(f"Totale: {len(clienti)} cliente/i")
        for c in clienti:
            print(f"  {c}")
