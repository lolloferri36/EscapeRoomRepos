from SERVICES.GESTORE_CATALOGO import GestoreCatalogo


class InterfacciaCatalogo:

    def __init__(self, gestore: GestoreCatalogo):
        self._gestore = gestore

    def mostraCatalogo(self) -> None:

        print("\n--- CATALOGO STANZE ---")
        stanze = self._gestore.elencaStanze()
        if not stanze:
            print("Nessuna stanza nel catalogo.")
            return
        for s in stanze:
            print(f"  {s}")

    def aggiornaStanza(self) -> None:

        print("\n--- AGGIORNA CATALOGO STANZE ---")
        self.mostraCatalogo()
        idStanza = input("\nID stanza da aggiornare: ").strip()
        nome = input("Nuovo nome: ").strip()
        tipo = input("Nuovo tipo: ").strip()
        descrizione = input("Nuova descrizione: ").strip()
        esito = self._gestore.aggiornaStanza(idStanza, nome, tipo, descrizione)
        print(f"\n→ {esito}")
