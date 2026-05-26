import unittest
import os
from SERVICES import GestoreCatalogo
from REPOSITORY import StanzaRepository
from MODELS import Stanza


class TestGestoreCatalogo(unittest.TestCase):
    
    def setUp(self):
        self.file_stanze = "test_stanze.json"
        self.stanza_repo = StanzaRepository(self.file_stanze)
        self.stanza_repo._stanze = {}
        
        self.gestore = GestoreCatalogo(self.stanza_repo)

        self.hints = [
            "Cerca nella libreria",
            "Guarda dietro lo specchio",
            "Controlla il cassetto"
        ]

        self.stanza1 = Stanza(
            "S001",
            "Camera oscura e misteriosa",  
            "50",                           
            "Stanza Horror",                
            "horror",                       
            True,                           
            self.hints
        )
        self.stanza_repo.aggiungi(self.stanza1)

        self.stanza2 = Stanza(
            "S002",
            "Stanza piena di enigmi",
            "60",
            "Escape Puzzle",
            "puzzle",
            True,
            ["Hint 1", "Hint 2"]
        )
        self.stanza_repo.aggiungi(self.stanza2)
    
    def tearDown(self):
        if os.path.exists(self.file_stanze):
            os.remove(self.file_stanze)
    
    def test_elenca_stanze_con_dati(self):

        stanze = self.gestore.elencaStanze()

        self.assertIsInstance(stanze, list)
        self.assertEqual(len(stanze), 2)
        
        ids_stanze = [s.getIdStanza() for s in stanze]
        self.assertIn("S001", ids_stanze)
        self.assertIn("S002", ids_stanze)
    
    def test_elenca_stanze_vuoto(self):

        self.stanza_repo._stanze = {}
        
        stanze = self.gestore.elencaStanze()
        
        self.assertIsInstance(stanze, list)
        self.assertEqual(len(stanze), 0)
    
    def test_elenca_stanze_ritorna_oggetti_corretti(self):

        stanze = self.gestore.elencaStanze()
        
        for stanza in stanze:
            self.assertIsInstance(stanza, Stanza)
    
    def test_aggiorna_stanza_successo(self):

        risultato = self.gestore.aggiornaStanza(
            idStanza="S001",
            nome="Camera Rinnovata",
            tipo="mystery",
            descrizione="Nuova stanza misteriosa"
        )
        
        self.assertIn("aggiornata con successo", risultato)
        self.assertIn("Camera Rinnovata", risultato)
        
        stanza = self.stanza_repo.trovaPerId("S001")
        self.assertEqual(stanza.getNome(), "Camera Rinnovata")
        self.assertEqual(stanza.getTipo(), "mystery")
        self.assertEqual(stanza.getDescrizione(), "Nuova stanza misteriosa")
    
    def test_aggiorna_stanza_verifica_salvataggio(self):
        
        self.gestore.aggiornaStanza("S002", "Nuovo Nome", "nuovo_tipo", "nuova desc")
        
        nuovo_repo = StanzaRepository(self.file_stanze)

        stanza_ricaricata = nuovo_repo.trovaPerId("S002")
        self.assertEqual(stanza_ricaricata.getNome(), "Nuovo Nome")
        self.assertEqual(stanza_ricaricata.getTipo(), "nuovo_tipo")
    
    def test_aggiorna_stanza_modifica_tutti_campi(self):

        stanza_prima = self.stanza_repo.trovaPerId("S001")
        nome_prima = stanza_prima.getNome()
        tipo_prima = stanza_prima.getTipo()
        desc_prima = stanza_prima.getDescrizione()
        
        self.gestore.aggiornaStanza(
            "S001",
            "Nome Completamente Nuovo",
            "Tipo Completamente Nuovo",
            "Descrizione Completamente Nuova"
        )

        stanza_dopo = self.stanza_repo.trovaPerId("S001")
        self.assertNotEqual(stanza_dopo.getNome(), nome_prima)
        self.assertNotEqual(stanza_dopo.getTipo(), tipo_prima)
        self.assertNotEqual(stanza_dopo.getDescrizione(), desc_prima)
        
        self.assertEqual(stanza_dopo.getNome(), "Nome Completamente Nuovo")
        self.assertEqual(stanza_dopo.getTipo(), "Tipo Completamente Nuovo")
        self.assertEqual(stanza_dopo.getDescrizione(), "Descrizione Completamente Nuova")

    
    def test_aggiorna_stanza_non_esistente(self):

        risultato = self.gestore.aggiornaStanza(
            idStanza="S999",  
            nome="Nome",
            tipo="Tipo",
            descrizione="Desc"
        )
        
        self.assertIn("Errore", risultato)
        self.assertIn("S999", risultato)
        self.assertIn("non trovata", risultato)
    
    def test_aggiorna_stanza_non_esistente_non_modifica_altre(self):

        stanza1_orig = self.stanza_repo.trovaPerId("S001")
        nome_orig = stanza1_orig.getNome()
        
        self.gestore.aggiornaStanza("S999", "Test", "Test", "Test")

        stanza1_dopo = self.stanza_repo.trovaPerId("S001")
        self.assertEqual(stanza1_dopo.getNome(), nome_orig)
    
    def test_completo_gestione_catalogo(self):

        stanze_prima = self.gestore.elencaStanze()
        self.assertEqual(len(stanze_prima), 2)
        
        risultato = self.gestore.aggiornaStanza(
            "S001",
            "Stanza Aggiornata",
            "nuovo_tipo",
            "nuova descrizione"
        )
        self.assertIn("aggiornata con successo", risultato)
        
        stanza = self.stanza_repo.trovaPerId("S001")
        self.assertEqual(stanza.getNome(), "Stanza Aggiornata")

        stanze_dopo = self.gestore.elencaStanze()
        self.assertEqual(len(stanze_dopo), 2)
        
        stanza_aggiornata = next(
            (s for s in stanze_dopo if s.getIdStanza() == "S001"),
            None
        )
        self.assertIsNotNone(stanza_aggiornata)
        self.assertEqual(stanza_aggiornata.getNome(), "Stanza Aggiornata")
    
    def test_aggiorna_multiple_stanze_sequenzialmente(self):

        ris1 = self.gestore.aggiornaStanza("S001", "Nome1", "Tipo1", "Desc1")
        self.assertIn("aggiornata", ris1)
        
        ris2 = self.gestore.aggiornaStanza("S002", "Nome2", "Tipo2", "Desc2")
        self.assertIn("aggiornata", ris2)
        
        s1 = self.stanza_repo.trovaPerId("S001")
        s2 = self.stanza_repo.trovaPerId("S002")
        
        self.assertEqual(s1.getNome(), "Nome1")
        self.assertEqual(s2.getNome(), "Nome2")
    
    def test_aggiorna_stanza_con_stringhe_vuote(self):
        risultato = self.gestore.aggiornaStanza("S001", "", "", "")

        self.assertIn("aggiornata con successo", risultato)
        
        stanza = self.stanza_repo.trovaPerId("S001")
        self.assertEqual(stanza.getNome(), "")
        self.assertEqual(stanza.getTipo(), "")
        self.assertEqual(stanza.getDescrizione(), "")


if __name__ == "__main__":
    unittest.main()