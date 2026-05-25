import unittest
from MODELS import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("01", "davide.doria06@gmail.com", "Davide77()", False)

    def test_email(self):
        self.assertEqual(self.cliente.getEmail(), "davide.doria06@gmail.com")

    def test_password(self):
        self.assertEqual(self.cliente.getPassword(), "Davide77()")

    def test_statoAccesso_default(self):
        self.assertFalse(self.cliente.getStatoAccesso())

    def test_idCliente(self):
        self.assertEqual(self.cliente.getIdCliente(), "01")

    def test_set_Accesso(self):
        self.cliente.setStatoAccesso(True)
        self.assertTrue(self.cliente.getStatoAccesso())

    def test_set_statoAccesso_false(self):
        self.cliente.setStatoAccesso(True)
        self.cliente.setStatoAccesso(False)
        self.assertFalse(self.cliente.getStatoAccesso())

    def test_tipo_errato_raises(self):
        with self.assertRaises(TypeError):
            self.cliente.setStatoAccesso("NotABoolean")

    def test_toDict(self):
        d = self.cliente.toDict()
        self.assertEqual(d["email"], "davide.doria06@gmail.com")
        self.assertEqual(d["password"], "Davide77()")
        self.assertFalse(d["statoAccesso"])
        self.assertEqual(d["idCliente"], "01")

    def test_fromDict(self):
        d = {"email": "luca.morelli@gmail.com", "password": "Luca88()", "statoAccesso": False, "idCliente": "02"}
        cliente = Cliente.fromDict(d)
        self.assertEqual(cliente.getIdCliente(), "02")
        self.assertEqual(cliente.getEmail(), "luca.morelli@gmail.com")
        self.assertEqual(cliente.getPassword(), "Luca88()")
        self.assertFalse(cliente.getStatoAccesso())

if __name__ == '__main__':
    unittest.main()