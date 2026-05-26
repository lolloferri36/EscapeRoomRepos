import uuid
from datetime import datetime, timedelta

from REPOSITORY.PRENOTAZIONE_REPOSITORY import PrenotazioneRepository
from REPOSITORY.STANZA_REPOSITORY import StanzaRepository
from MODELS.PRENOTAZIONE import Prenotazione


class GestorePrenotazione:

    ORARI_DISPONIBILI = [
        "09:00", "10:30", "12:00", "13:30", "15:00",
        "16:30", "18:00", "19:30", "21:00"
    ]

    def __init__(self, pren_repo: PrenotazioneRepository,
                 stanza_repo: StanzaRepository):
        self._pren_repo = pren_repo
        self._stanza_repo = stanza_repo

    def prenota(self, idCliente: str, idStanza: str, giorno: str, ora: str) -> str:
        try:
            giorno_ora_pren = datetime.strptime(f"{giorno} {ora}", "%Y-%m-%d %H:%M")  
        except ValueError:
            return "Errore: formato non valido. Usa YYYY-MM-DD e HH:MM"
        if giorno_ora_pren <= datetime.now():
            return "Errore: non è possibile prenotare per un orario già trascorso"

        try:
            self._stanza_repo.trovaPerId(idStanza)
        except KeyError:
            return f"Errore: stanza '{idStanza}' non trovata"

        occupate = self._pren_repo.trovaAttivePerStanzaEGiorno(idStanza, giorno)
        for p in occupate:
            if p.getOra() == ora:
                return "Errore: stanza già occupata in questa fascia oraria"

        nuova = Prenotazione(str(uuid.uuid4()), idCliente, idStanza, True, giorno, ora)
        self._pren_repo.aggiungi(nuova)
        return (f"Prenotazione confermata!\n"
                f"  Stanza: {idStanza} — {giorno} alle {ora}\n"
                f"  ID prenotazione: {nuova.getIdPrenotazione()}")

    def disdetta(self, idPrenotazione: str, idCliente: str) -> str:
        try:
            pren = self._pren_repo.trovaPerId(idPrenotazione)
        except KeyError:
            return "Errore: prenotazione non trovata"
        if pren.getIdCliente() != idCliente:
            return "Errore: prenotazione non appartenente al cliente corrente"
        if pren.getStatoDisdetta() is True:
            return "Errore: prenotazione già disdetta"
        giorno, ora = pren.getGiornoOra()
        try:
            giorno_ora_pren = datetime.strptime(f"{giorno} {ora}", "%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            return "Errore: formato data/ora della prenotazione non valido"
        if giorno_ora_pren - datetime.now() < timedelta(hours=24):
            return "Errore: disdetta non consentita — mancano meno di 24 ore all'inizio"
        pren.setStatoDisdetta(True)
        self._pren_repo.aggiorna(pren)
        return "Disdetta confermata. Speriamo di rivederti presto!"

    def modificaPrenotazione(self, idPrenotazione: str, idCliente: str,
                              nuovo_giorno: str, nuova_ora: str) -> str:
        try:
            pren = self._pren_repo.trovaPerId(idPrenotazione)
        except KeyError:
            return "Errore: prenotazione non trovata"
        if pren.getIdCliente() != idCliente:
            return "Errore: prenotazione non appartenente al cliente corrente"
        if pren.getStatoDisdetta() is True:
            return "Errore: impossibile modificare una prenotazione disdetta"
        giorno, ora = pren.getGiornoOra()
        try:
            giorno_ora_pren = datetime.strptime(f"{giorno} {ora}", "%Y-%m-%d %H:%M")
        except (ValueError, TypeError):
            return "Errore: formato data/ora della prenotazione non valido"
        if giorno_ora_pren - datetime.now() < timedelta(hours=24):
            return "Errore: modifica non consentita — mancano meno di 24 ore all'inizio"
        try:
            giorno_ora_nuovo = datetime.strptime(f"{nuovo_giorno} {nuova_ora}", "%Y-%m-%d %H:%M")
        except ValueError:
            return "Errore: formato non valido. Usa YYYY-MM-DD e HH:MM"
        if giorno_ora_nuovo <= datetime.now():
            return "Errore: non è possibile spostare la prenotazione in un orario passato"
        occupate = self._pren_repo.trovaAttivePerStanzaEGiorno(pren.getIdStanza(), nuovo_giorno)
        for p in occupate:
            if p.getOra() == nuova_ora and p.getIdPrenotazione() != idPrenotazione:
                return "Errore: stanza già occupata nel nuovo orario richiesto"
        pren.setGiornoOra(nuovo_giorno, nuova_ora)
        self._pren_repo.aggiorna(pren)
        return f"Prenotazione aggiornata: {nuovo_giorno} alle {nuova_ora}"

    def elencaPrenotazioniCliente(self, idCliente: str) -> list:
        return self._pren_repo.trovaPerCliente(idCliente)

    def elencaTuttePrenotazioni(self) -> list:
        return self._pren_repo.tutti()
