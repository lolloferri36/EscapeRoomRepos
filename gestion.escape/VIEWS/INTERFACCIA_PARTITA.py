from SERVICES.GESTORE_PARTITA import GestorePartita
from SERVICES.GESTORE_PRENOTAZIONE import GestorePrenotazione


class InterfacciaPartita:

    def __init__(self, gestore: GestorePartita, gestore_pren: GestorePrenotazione):
        self._gestore = gestore
        self._gestore_pren = gestore_pren

    def avviaPartita(self, idCliente: str) -> None:

        print("\n--- AVVIA PARTITA ---")
        prenotazioni = self._gestore_pren.elencaPrenotazioniCliente(idCliente)
        if not prenotazioni:
            print("→ Nessuna prenotazione attiva su cui avviare una partita.")
            return
        print("Le tue prenotazioni:")
        for p in prenotazioni:
            print(f"  {p}")
        idPrefisso = input("\nInserisci i primi 8 caratteri dell'ID prenotazione: ").strip()

        pren_trovata = None
        for p in prenotazioni:
            if p.getIdPrenotazione().startswith(idPrefisso):
                pren_trovata = p
                break
        if pren_trovata is None:
            print("→ Prenotazione non trovata.")
            return
        _,msg = self._gestore.avviaPartita(pren_trovata.getIdPrenotazione(), idCliente)   #_ perchè a noi interessa solo il msg di esito quindi uso il trattino per ignorare la partita restituita
        print(f"\n→ {msg}")

    def terminaPartita(self) -> None:

        print("\n--- TERMINA PARTITA ---")
        esito = self._gestore.terminaPartita()
        print(f"\n→ {esito}")

    def abbandonaPartita(self) -> None:

        print("\n--- ABBANDONA PARTITA ---")
        conferma = input("Sei sicuro di voler abbandonare? L'esito sarà registrato come sconfitta. (s/n): ").strip().lower()
        if conferma != "s":
            print("→ Abbandono annullato.")
            return
        esito = self._gestore.abbandonaPartita()
        print(f"\n→ {esito}")

    def chiediSuggerimento(self) -> None:

        print("\n--- CHIEDI SUGGERIMENTO ---")
        risultato = self._gestore.chiediSuggerimento()
        print(f"\n→ {risultato}")

    def visualizzaStoricoPartite(self, idCliente: str) -> None:

        print("\n--- STORICO PARTITE ---")
        storico = self._gestore.elencaStoricoPartite(idCliente)
        if not storico:
            print("→ Nessuna partita terminata.")
            return
        print("Le tue partite terminate:")
        for p in storico:
            print(f"  {p}")
