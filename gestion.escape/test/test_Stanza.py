import unittest
from MODELS import Stanza

class TestStanza(unittest.TestCase):

    def setUp(self):
        hints = [
            "Cerca nella libreria",
            "Guarda dietro allo specchio",
            "controlla il cassetto",
        ]
        self.stanza= Stanza("01", "camera chiusa", "50", "room", "horror", True, hints )
        
    def test_idStanza(self):
        self.assertEqual(self.stanza.getIdStanza(), "01")

    def test_descrizione(self):
        self.assertEqual(self.stanza.getDescrizione(), "camera chiusa")

    def test_prezzo(self):
        self.assertEqual(self.stanza.getPrezzo(), "50")

    def test_nome(self):
        self.assertEqual(self.stanza.getNome(), "room")

    def test_tipo(self):
        self.assertEqual(self.stanza.getTipo(), "horror")

    def test_suggerimenti(self):
        hints = [
            "Cerca nella libreria",
            "Guarda dietro allo specchio",
            "controlla il cassetto",
        ]
  
    def test_stato_default(self):
        self.assertTrue(self.stanza.isDisponibile())

    def test_setStato(self):
        self.stanza.setStato(False)
        self.assertFalse(self.stanza.isDisponibile())

    def test_setStato_true(self):
        self.stanza.setStato(False)
        self.stanza.setStato(True)
        self.assertTrue(self.stanza.isDisponibile())

    def test_tipo_errato_raises_statoPren(self):
        with self.assertRaises(TypeError):
            self.stanza.setStato("NotABoolean")

    def test_set_dati_stanze(self):

        self.assertEqual(self.stanza.getNome(), "room")
        self.assertEqual(self.stanza.getTipo(), "horror")
        self.assertEqual(self.stanza.getDescrizione(), "camera chiusa")
    
        self.stanza.setDatiStanze("escape room", "puzzle", "stanza luminosa")
    
        self.assertEqual(self.stanza.getNome(), "escape room")
        self.assertEqual(self.stanza.getTipo(), "puzzle")
        self.assertEqual(self.stanza.getDescrizione(), "stanza luminosa")        
 
    def test_toDict(self):

        hints = [
            "Cerca nella libreria",
            "Guarda dietro allo specchio",
            "controlla il cassetto",
        ]

        d = self.stanza.toDict()
        self.assertEqual(d["idStanza"], "01")
        self.assertEqual(d["descrizione"], "camera chiusa")
        self.assertEqual(d["prezzo"], "50")
        self.assertEqual(d["nome"], "room")
        self.assertEqual(d["tipo"], "horror")
        self.assertTrue(d["stato"])
        self.assertEqual(d["suggerimenti"], hints)

    def test_from_dict(self):

        hints2 = [
            "Cerca nella libreria2",
            "Guarda dietro allo specchio2",
            "controlla il cassetto2",
        ]

        d = { "idStanza": "02", "descrizione": "camera2 chiusa", "prezzo": "60", "nome": "room2", "tipo": "giallo", "stato": True, "suggerimenti": hints2}
        stanza= Stanza.fromDict(d)
        self.assertEqual(stanza.getIdStanza(), "02")
        self.assertEqual(stanza.getDescrizione(), "camera2 chiusa")
        self.assertEqual(stanza.getPrezzo(), "60")
        self.assertEqual(stanza.getNome(), "room2")
        self.assertEqual(stanza.getTipo(), "giallo")
        self.assertTrue(stanza.isDisponibile())
        self.assertEqual(stanza.getSuggerimenti(), hints2)

if __name__ == '__main__':
    unittest.main()

       