import unittest
from MODELS import Prenotazione


class TestPrenotazione(unittest.TestCase):

    def setUp(self):
        self.prenotazione = Prenotazione("01", "01", "01", False, "2026-12-15", "14:30", False)
        
    def test_idPrenotazione(self):
        self.assertEqual(self.prenotazione.getIdPrenotazione(), "01")

    def test_idCliente(self):
        self.assertEqual(self.prenotazione.getIdCliente(), "01")

    def test_idStanza(self):
        self.assertEqual(self.prenotazione.getIdStanza(), "01")

    def test_giorno(self):
        self.assertEqual(self.prenotazione.getGiorno(), "2026-12-15")

    def test_ora(self):
        self.assertEqual(self.prenotazione.getOra(), "14:30")

    def test_statoPrenotazione_default(self):
        self.assertFalse(self.prenotazione.getStatoPrenotazione())

    def test_statoDisdetta_default(self):
        self.assertFalse(self.prenotazione.getStatoDisdetta())

    def test_giornoOra(self):
        giorno_ora = self.prenotazione.getGiornoOra()
        self.assertIsInstance(giorno_ora, tuple)
        self.assertEqual(len(giorno_ora), 2)
        self.assertEqual(giorno_ora[0], "2026-12-15")
        self.assertEqual(giorno_ora[1], "14:30")

    def test_set_statoPrenotazione(self):
        self.prenotazione.setStatoPrenotazione(True)
        self.assertTrue(self.prenotazione.getStatoPrenotazione())

    def test_set_statoPrenotazione_false(self):
        self.prenotazione.setStatoPrenotazione(True)
        self.prenotazione.setStatoPrenotazione(False)
        self.assertFalse(self.prenotazione.getStatoPrenotazione())

    def test_tipo_errato_raises_statoPren(self):
        with self.assertRaises(TypeError):
            self.prenotazione.setStatoPrenotazione("NotABoolean")

    def test_set_statoDisdetta(self):
        self.prenotazione.setStatoDisdetta(True)
        self.assertTrue(self.prenotazione.getStatoDisdetta())

    def test_set_statoDisdetta_false(self):
        self.prenotazione.setStatoDisdetta(True)
        self.prenotazione.setStatoDisdetta(False)
        self.assertFalse(self.prenotazione.getStatoDisdetta())

    def test_tipo_errato_raises_statoDisd(self):
        with self.assertRaises(TypeError):
            self.prenotazione.setStatoDisdetta("NotABoolean")
 
    def test_toDict(self):
        d = self.prenotazione.toDict()
        self.assertEqual(d["idPrenotazione"], "01")
        self.assertEqual(d["idCliente"], "01")
        self.assertEqual(d["idStanza"], "01")
        self.assertFalse(d["statoPrenotazione"])
        self.assertEqual(d["giorno"], "2026-12-15")
        self.assertEqual(d["ora"], "14:30")
        self.assertFalse(d["statoDisdetta"])

    def test_from_dict(self):
        d = { "idPrenotazione": "02", "idCliente": "02", "idStanza": "02", "statoPrenotazione": False, "giorno": "2026-11-25", "ora": "15:30", "statoDisdetta": False}
        prenotazione = Prenotazione.fromDict(d)
        self.assertEqual(prenotazione.getIdPrenotazione(), "02")
        self.assertEqual(prenotazione.getIdCliente(), "02")
        self.assertEqual(prenotazione.getIdStanza(), "02")
        self.assertFalse(prenotazione.getStatoPrenotazione())
        self.assertEqual(prenotazione.getGiorno(), "2026-11-25")
        self.assertEqual(prenotazione.getOra(), "15:30")
        self.assertFalse(prenotazione.getStatoDisdetta())

if __name__ == '__main__':
    unittest.main()

