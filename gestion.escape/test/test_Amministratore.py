import unittest
from MODELS import Amministratore

class TestAmministratore(unittest.TestCase):

    def setUp(self):
        self.amministratore = Amministratore("ADM001", "admin@escape.it", "Admin123!", False)

    def test_idAdmin(self):
        self.assertEqual(self.amministratore.getIdAdmin(), "ADM001")

    def test_email(self):
        self.assertEqual(self.amministratore.getEmail(), "admin@escape.it")

    def test_password(self):
        self.assertEqual(self.amministratore.getPassword(), "Admin123!")

    def test_statoAccesso_default(self):
        self.assertFalse(self.amministratore.getStatoAccesso())

    def test_set_Accesso(self):
        self.amministratore.setStatoAccesso(True)
        self.assertTrue(self.amministratore.getStatoAccesso())

    def test_set_statoAccesso_false(self):
        self.amministratore.setStatoAccesso(True)
        self.amministratore.setStatoAccesso(False)
        self.assertFalse(self.amministratore.getStatoAccesso())

    def test_tipo_errato_raises(self):
        with self.assertRaises(TypeError):
            self.amministratore.setStatoAccesso("NotABoolean")
            
    def test_toDict(self):
        d = self.amministratore.toDict()
        self.assertEqual(d["idAdmin"], "ADM001")
        self.assertEqual(d["email"], "admin@escape.it")
        self.assertEqual(d["password"], "Admin123!")
        self.assertFalse(d["statoAccesso"])

    def test_fromDict(self):
        d = {"idAdmin": "ADM002", "email": "admin2@escape.it", "password": "Admin456!", "statoAccesso": False}
        admin = Amministratore.fromDict(d)
        self.assertEqual(admin.getIdAdmin(), "ADM002")
        self.assertEqual(admin.getEmail(), "admin2@escape.it")
        self.assertEqual(admin.getPassword(), "Admin456!")
        self.assertFalse(admin.getStatoAccesso())

if __name__ == '__main__':
    unittest.main()