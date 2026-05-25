from REPOSITORY.AMMINISTRATORE_REPOSITORY import AmministratoreRepository
from REPOSITORY.CLIENTE_REPOSITORY import ClienteRepository
from REPOSITORY.PRENOTAZIONE_REPOSITORY import PrenotazioneRepository
from REPOSITORY.STANZA_REPOSITORY import StanzaRepository
from REPOSITORY.PARTITA_REPOSITORY import PartitaRepository

from SERVICES.GESTORE_ACCOUNT import GestoreAccount
from SERVICES.GESTORE_CATALOGO import GestoreCatalogo
from SERVICES.GESTORE_CLIENTE import GestoreCliente
from SERVICES.GESTORE_PRENOTAZIONE import GestorePrenotazione
from SERVICES.GESTORE_PARTITA import GestorePartita

from VIEWS.INTERFACCIA_ACCOUNT import InterfacciaAccount
from VIEWS.INTERFACCIA_CATALOGO import InterfacciaCatalogo
from VIEWS.INTERFACCIA_CLIENTE import InterfacciaCliente
from VIEWS.INTERFACCIA_PARTITA import InterfacciaPartita
from VIEWS.INTERFACCIA_PRENOTAZIONE import InterfacciaPrenotazione

from MODELS.CLIENTE import Cliente
from MODELS.AMMINISTRATORE import Amministratore

DATA = "DATA(JSON)"


def main():

   
    admin_repo   = AmministratoreRepository(f"{DATA}/AMMINISTRATORE.json")
    cliente_repo = ClienteRepository(f"{DATA}/CLIENTI.json")
    pren_repo    = PrenotazioneRepository(f"{DATA}/PRENOTAZIONI.json")
    stanza_repo  = StanzaRepository(f"{DATA}/STANZE.json")
    partita_repo = PartitaRepository(f"{DATA}/PARTITE.json")

    gestore_account  = GestoreAccount(admin_repo, cliente_repo)
    gestore_catalogo = GestoreCatalogo(stanza_repo)
    gestore_cliente  = GestoreCliente(cliente_repo)
    gestore_pren     = GestorePrenotazione(pren_repo, stanza_repo)
    gestore_partita  = GestorePartita(partita_repo, pren_repo, stanza_repo)

    interfaccia_account  = InterfacciaAccount(gestore_account)
    interfaccia_catalogo = InterfacciaCatalogo(gestore_catalogo)
    interfaccia_cliente  = InterfacciaCliente(gestore_cliente)
    interfaccia_pren     = InterfacciaPrenotazione(gestore_pren, gestore_catalogo)
    interfaccia_partita  = InterfacciaPartita(gestore_partita, gestore_pren)

    utente_corrente = None

    print("=" * 45)
    print("  Benvenuto nel sistema Escape Room!")
    print("=" * 45)

    while True:
        print()

        if utente_corrente is None:

            print("=== MENU PRINCIPALE ===")
            print("1. Consulta catalogo stanze")
            print("2. Accedi come Cliente")
            print("3. Accedi come Amministratore")
            print("4. Registrati")
            print("0. Esci")
            scelta = input("Scelta: ").strip()

            if scelta == "1":
                interfaccia_catalogo.mostraCatalogo()
            elif scelta == "2":
                utente_corrente = interfaccia_account.accediCliente()
            elif scelta == "3":
                utente_corrente = interfaccia_account.accediAmministratore()
            elif scelta == "4":
                interfaccia_account.registra()
            elif scelta == "0":
                print("Arrivederci!")
                break

        elif isinstance(utente_corrente, Cliente):
            print(f"=== AREA CLIENTE — {utente_corrente.getEmail()} ===")
            print("1.  Consulta catalogo stanze")
            print("2.  Le mie prenotazioni")
            print("3.  Prenota stanza")
            print("4.  Disdetta prenotazione")
            print("5.  Modifica prenotazione")
            print("6.  Avvia partita")
            print("7.  Termina partita")
            print("8.  Chiedi suggerimento")
            print("9.  Abbandona partita")
            print("10. Storico partite giocate")
            print("0.  Logout")
            scelta = input("Scelta: ").strip()

            if scelta == "1":
                interfaccia_catalogo.mostraCatalogo()
            elif scelta == "2":
                interfaccia_pren.mostraPrenotazioniCliente(utente_corrente.getIdCliente())
            elif scelta == "3":
                interfaccia_pren.prenota(utente_corrente.getIdCliente())
            elif scelta == "4":
                interfaccia_pren.disdetta(utente_corrente.getIdCliente())
            elif scelta == "5":
                interfaccia_pren.modifica(utente_corrente.getIdCliente())
            elif scelta == "6":
                interfaccia_partita.avviaPartita(utente_corrente.getIdCliente())
            elif scelta == "7":
                interfaccia_partita.terminaPartita()
            elif scelta == "8":
                interfaccia_partita.chiediSuggerimento()
            elif scelta == "9":
                interfaccia_partita.abbandonaPartita()
            elif scelta == "10":
                interfaccia_partita.visualizzaStoricoPartite(utente_corrente.getIdCliente())
            elif scelta == "0":
                utente_corrente.setStatoAccesso(False)
                utente_corrente = None
                print("→ Logout effettuato.")

        elif isinstance(utente_corrente, Amministratore):
            print(f"=== AREA AMMINISTRATORE — {utente_corrente.getEmail()} ===")
            print("1. Visualizza clienti registrati")
            print("2. Visualizza tutte le prenotazioni")
            print("3. Aggiorna catalogo stanze")
            print("0. Logout")
            scelta = input("Scelta: ").strip()

            if scelta == "1":
                interfaccia_cliente.mostraClienti()
            elif scelta == "2":
                interfaccia_pren.mostraTuttePrenotazioni()
            elif scelta == "3":
                interfaccia_catalogo.aggiornaStanza()
            elif scelta == "0":
                utente_corrente.setStatoAccesso(False)
                utente_corrente = None
                print("→ Logout effettuato.")


if __name__ == "__main__":
    main()
