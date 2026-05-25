import unittest
from datetime import datetime, timedelta
from MODELS import Partita


class TestPartita(unittest.TestCase):

    def setUp(self):
        self.partita = Partita("01", "01", "01", "vittoria", datetime(2026, 12, 15, 16, 30), datetime(2026, 12, 15, 16, 40))
    
    def test_idPartita(self):
        self.assertEqual(self.partita.getIdPartita(), "01")

    def test_idCliente(self):
        self.assertEqual(self.partita.getIdCliente(), "01")

    def test_idPrenotazione(self):
        self.assertEqual(self.partita.getIdPrenotazione(), "01")

    def test_esito(self):
        self.assertEqual(self.partita.getEsito(), "vittoria")
   
    def test_avviaPartita(self):
        partita = Partita("01", "01", "01")
        self.assertFalse(partita.isAvviata())
        partita.avvia()
        self.assertTrue(partita.isAvviata())

    def test_terminaPartita(self):
        partita = Partita("02", "02", "02")
        
        self.assertIsNone(partita._tempoInizio)
        self.assertIsNone(partita._tempoFine)
        self.assertFalse(partita.isAvviata())
        
        partita.avvia()

        self.assertIsNotNone(partita._tempoInizio)
        self.assertIsNone(partita._tempoFine)
        self.assertTrue(partita.isAvviata())

        esito = partita.termina()

        self.assertIn(esito, ["vittoria", "sconfitta"])
        self.assertIsNotNone(partita._tempoFine)
        self.assertFalse(partita.isAvviata())
        self.assertEqual(partita.getEsito(), esito)

    def test_abbandonaPartita(self):
        partita = Partita("03", "03", "03")
        
        self.assertIsNone(partita._tempoInizio)
        self.assertIsNone(partita._tempoFine)
        self.assertFalse(partita.isAvviata())
        
        partita.avvia()

        self.assertIsNotNone(partita._tempoInizio)
        self.assertIsNone(partita._tempoFine)
        self.assertTrue(partita.isAvviata())

        esito = partita.abbandona()

        self.assertIn(esito, "sconfitta")
        self.assertEqual(partita.getEsito(), "sconfitta")
        self.assertIsNotNone(partita._tempoFine)
        self.assertFalse(partita.isAvviata())

    
    def test_chiediSuggerimento(self):
        partita = Partita ("04", "04", "04")
        suggerimenti = [
            "Cerca nella libreria",
            "Guarda dietro allo specchio",
            "controlla il cassetto",
        ]

        self.assertEqual(partita._indiceSuggerimento, 0, "indice deve iniziare a 0")
        hint1 = partita.chiediSuggerimento(suggerimenti)
        self.assertIn("Cerca nella libreria", hint1)
        self.assertIn("💡 Suggerimento 1/3", hint1)
        self.assertIn("Suggerimenti rimanenti: 2", hint1)

        self.assertEqual(partita._indiceSuggerimento, 1)

        hint2 = partita.chiediSuggerimento(suggerimenti)
        self.assertIn("Guarda dietro allo specchio", hint2)
        self.assertIn("💡 Suggerimento 2/3", hint2)
        self.assertIn("rimanenti: 1", hint2)

        self.assertEqual(partita._indiceSuggerimento, 2)

        hint3 = partita.chiediSuggerimento(suggerimenti)
        self.assertIn("controlla il cassetto", hint3)
        self.assertIn("💡 Suggerimento 3/3", hint3)
        self.assertIn("Suggerimenti rimanenti: 0", hint3)

        self.assertEqual(partita._indiceSuggerimento, 3)

        hint4 = partita.chiediSuggerimento(suggerimenti)
        self.assertEqual(hint4, "Hai già ricevuto tutti i suggerimenti disponibili per questa stanza.")
        self.assertEqual(partita._indiceSuggerimento, 3, "indice non deve incrementare oltre il limite")
    
    def test_is_avviata_true(self):
        partita = Partita("05", "05", "05")
        partita.avvia()
        self.assertTrue(partita.isAvviata())

    def test_is_avviata_false(self):
        partita = Partita("06", "06", "06")
        self.assertFalse(partita.isAvviata())
    
    def test_toDict(self):
        d = self.partita.toDict()
        
        self.assertEqual(d["idPartita"], "01")
        self.assertEqual(d["idCliente"], "01")
        self.assertEqual(d["idPrenotazione"], "01")
        self.assertEqual(d["esito"], "vittoria")
        self.assertEqual(d["tempoInizio"], "2026-12-15T16:30:00")
        self.assertEqual(d["tempoFine"], "2026-12-15T16:40:00")

    def test_fromDict(self):
        d = {"idPartita": "07", "idCliente": "07", "idPrenotazione": "07", "esito": "sconfitta"}
        partita = Partita.fromDict(d)
        
        self.assertEqual(partita.getIdPartita(), "07")
        self.assertEqual(partita.getIdCliente(), "07")
        self.assertEqual(partita.getEsito(), "sconfitta")

if __name__ == "__main__":
    unittest.main()