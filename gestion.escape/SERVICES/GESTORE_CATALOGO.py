from REPOSITORY.STANZA_REPOSITORY import StanzaRepository


class GestoreCatalogo:

    def __init__(self, stanza_repo: StanzaRepository):
        self._stanza_repo = stanza_repo

    def elencaStanze(self) -> list:
        return self._stanza_repo.tutti()

    def aggiornaStanza(self, idStanza: str, nome: str, tipo: str, descrizione: str) -> str:
        try:
            stanza = self._stanza_repo.trovaPerId(idStanza)
        except KeyError:     #serve a rilevare l'errore quando 
            return f"Errore: stanza '{idStanza}' non trovata"
        stanza.setDatiStanze(nome, tipo, descrizione)
        self._stanza_repo.salva()
        return f"Stanza '{nome}' aggiornata con successo"
