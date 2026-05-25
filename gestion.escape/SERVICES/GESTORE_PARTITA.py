import uuid
from typing import Optional, Tuple

from REPOSITORY.PARTITA_REPOSITORY import PartitaRepository
from REPOSITORY.PRENOTAZIONE_REPOSITORY import PrenotazioneRepository
from REPOSITORY.STANZA_REPOSITORY import StanzaRepository
from MODELS.PARTITA import Partita


class GestorePartita:

    def __init__(self, partita_repo: PartitaRepository,
                 pren_repo: PrenotazioneRepository,
                 stanza_repo: StanzaRepository):
        self._partita_repo = partita_repo
        self._pren_repo = pren_repo
        self._stanza_repo = stanza_repo
        self._partita_corrente: Optional[Partita] = None

    def avviaPartita(self, idPrenotazione: str, idCliente: str) -> Tuple[Optional[Partita], str]:
        try:
            pren = self._pren_repo.trovaPerId(idPrenotazione)
        except KeyError:
            return None, "Errore: prenotazione non trovata"
        if pren.getIdCliente() != idCliente:
            return None, "Errore: prenotazione non appartenente al cliente"
        if pren.getStatoDisdetta() is True:
            return None, "Errore: prenotazione disdetta, impossibile avviare la partita"
        if self._partita_corrente is not None and self._partita_corrente.isAvviata():
            return None, "Errore: c'è già una partita in corso"

        partita = Partita(str(uuid.uuid4()), idCliente, idPrenotazione)
        partita.avvia()
        self._partita_corrente = partita
        return partita, "Partita avviata! Il cronometro è in marcia. Buona fortuna!"

    def terminaPartita(self) -> str:
        if self._partita_corrente is None or not self._partita_corrente.isAvviata():
            return "Errore: nessuna partita in corso da terminare"

        esito = self._partita_corrente.termina()
        self._partita_repo.aggiungi(self._partita_corrente)
        self._partita_corrente = None

        if esito == "vittoria":
            return "Complimenti, hai vinto la partita! 🏆"
        else:
            return "La partita è terminata. Purtroppo hai perso, ma non demordere! ❌"

    def abbandonaPartita(self) -> str:
        if self._partita_corrente is None or not self._partita_corrente.isAvviata():
            return "Errore: nessuna partita in corso da abbandonare"

        self._partita_corrente.abbandona()
        self._partita_repo.aggiungi(self._partita_corrente)
        self._partita_corrente = None

        return "Hai abbandonato la partita. Esito registrato come sconfitta. ❌"

    def chiediSuggerimento(self) -> str:
        if self._partita_corrente is None or not self._partita_corrente.isAvviata():
            return "Errore: nessuna partita in corso."

        idPrenotazione = self._partita_corrente.getIdPrenotazione()
        try:
            pren = self._pren_repo.trovaPerId(idPrenotazione)
        except KeyError:
            return "Errore: prenotazione non trovata."

        try:
            stanza = self._stanza_repo.trovaPerId(pren.getIdStanza())
        except KeyError:
            return "Errore: stanza non trovata."

        suggerimenti = stanza.getSuggerimenti()
        return self._partita_corrente.chiediSuggerimento(suggerimenti)

    def elencaStoricoPartite(self, idCliente: str) -> list:
        return self._partita_repo.trovaStoricoPerCliente(idCliente)
