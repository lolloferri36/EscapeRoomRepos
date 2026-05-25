import unittest
from MODELS import Utente

class TestUtente(unittest.TestCase):

    def setUp(self):
        self.utente = Utente("mario.rossi@gmail.com", "123", False)

    def test_email(self):
        self.assertEqual(self.utente.getEmail(), "mario.rossi@gmail.com")

    def test_password(self):
        self.assertEqual(self.utente.getPassword(), "123")

    def test_statoAccesso_default(self):
        self.assertFalse(self.utente.getStatoAccesso())

    def test_set_Accesso(self):
        self.utente.setStatoAccesso(True)
        self.assertTrue(self.utente.getStatoAccesso())

    def test_set_statoAccesso_false(self):
        self.utente.setStatoAccesso(True)
        self.utente.setStatoAccesso(False)
        self.assertFalse(self.utente.getStatoAccesso())

    def test_tipo_errato_raises(self):
        with self.assertRaises(TypeError):
            self.utente.setStatoAccesso("NotABoolean")

    def test_toDict(self):
        d = self.utente.toDict()
        self.assertEqual(d["email"], "mario.rossi@gmail.com")
        self.assertEqual(d["password"], "123")
        self.assertFalse(d["statoAccesso"])

    def test_fromDict(self):
        d = {"email": "lorenzo.ferri@gmail.com", "password": "Lorenzo99()", "statoAccesso": False}
        utente = Utente.fromDict(d)
        self.assertEqual(utente.getEmail(), "lorenzo.ferri@gmail.com")
        self.assertEqual(utente.getPassword(), "Lorenzo99()")
        self.assertFalse(utente.getStatoAccesso())

if __name__ == '__main__':
    unittest.main()