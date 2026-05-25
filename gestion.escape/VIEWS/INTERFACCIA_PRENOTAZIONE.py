from SERVICES.GESTORE_PRENOTAZIONE import GestorePrenotazione
from SERVICES.GESTORE_CATALOGO import GestoreCatalogo


class InterfacciaPrenotazione:

    def __init__(self, gestore: GestorePrenotazione, gestore_catalogo: GestoreCatalogo):
        self._gestore = gestore
        self._gestore_catalogo = gestore_catalogo

    def mostraPrenotazioniCliente(self, idCliente: str) -> None:

        print("\n--- LE MIE PRENOTAZIONI ---")
        prenotazioni = self._gestore.elencaPrenotazioniCliente(idCliente)
        if not prenotazioni:
            print("Nessuna prenotazione attiva.")
            return
        for p in prenotazioni:
            print(f"  {p}")

    def prenota(self, idCliente: str) -> None:

        print("\n--- PRENOTA STANZA ---")
        stanze = self._gestore_catalogo.elencaStanze()
        print("Stanze disponibili:")
        for s in stanze:
            print(f"  {s}")
        print("\nFasce orarie disponibili (90 min ciascuna):")
        print("  " + "  |  ".join(GestorePrenotazione.ORARI_DISPONIBILI))
        idStanza = input("ID stanza: ").strip()
        giorno = input("Giorno (YYYY-MM-DD): ").strip()
        ora = input("Ora di inizio: ").strip()
        esito = self._gestore.prenota(idCliente, idStanza, giorno, ora)
        print(f"\n→ {esito}")

    def disdetta(self, idCliente: str) -> None:

        print("\n--- DISDETTA PRENOTAZIONE ---")
        self.mostraPrenotazioniCliente(idCliente)
        idPrefisso = input("\nInserisci i primi 8 caratteri dell'ID prenotazione: ").strip()
        pren = self._trovaPerId(idCliente, idPrefisso)
        if pren is None:
            print("→ Prenotazione non trovata.")
            return
        esito = self._gestore.disdetta(pren.getIdPrenotazione(), idCliente)
        print(f"\n→ {esito}")

    def modifica(self, idCliente: str) -> None:

        print("\n--- MODIFICA PRENOTAZIONE ---")
        self.mostraPrenotazioniCliente(idCliente)
        idPrefisso = input("\nInserisci i primi 8 caratteri dell'ID prenotazione: ").strip()
        pren = self._trovaPerId(idCliente, idPrefisso)
        if pren is None:
            print("→ Prenotazione non trovata.")
            return
        print(f"  Prenotazione corrente: {pren}")
        print("  Fasce orarie disponibili:")
        print("  " + "  |  ".join(GestorePrenotazione.ORARI_DISPONIBILI))
        nuovo_giorno = input("Nuovo giorno (YYYY-MM-DD): ").strip()
        nuova_ora = input("Nuova ora di inizio: ").strip()
        esito = self._gestore.modificaPrenotazione(
            pren.getIdPrenotazione(), idCliente, nuovo_giorno, nuova_ora)
        print(f"\n→ {esito}")

    def mostraTuttePrenotazioni(self) -> None:

        print("\n--- TUTTE LE PRENOTAZIONI ---")
        prenotazioni = self._gestore.elencaTuttePrenotazioni()
        if not prenotazioni:
            print("Nessuna prenotazione nel sistema.")
            return
        print(f"Totale: {len(prenotazioni)} prenotazione/i")
        for p in prenotazioni:
            print(f"  {p}")

    def _trovaPerId(self, idCliente: str, prefisso: str) -> None:
        for p in self._gestore.elencaPrenotazioniCliente(idCliente):
            if p.getIdPrenotazione().startswith(prefisso):
                return p
        return None
