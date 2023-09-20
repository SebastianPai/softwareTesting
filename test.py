#Integrantes: 
# - Jhon Sebastian Pai
#- Jhon Brayan Muñoz
#- Jhonatan Vasquez
#- Kedin Benavides

import unittest
import re
from datetime import datetime
import tarjeta2 as sh

class string_handlerTest(unittest.TestCase):
    def test_validar_tarjeta(self):
        self.assertTrue(sh.validar_tarjeta("1234567891234567"))
        self.assertFalse(sh.validar_tarjeta("12345678"))
        self.assertFalse(sh.validar_tarjeta("124567"))
        self.assertTrue(sh.validar_tarjeta("1234567891231257"))
    def test_validar_fecha(self):
        self.assertTrue(sh.validar_fecha("10/23"))
        self.assertFalse(sh.validar_fecha("5/23"))
        self.assertFalse(sh.validar_fecha("15/23"))
    def test_validar_codigo(self):
        self.assertTrue(sh.validar_codigo("123"))
        self.assertFalse(sh.validar_codigo("1234"))
        self.assertFalse(sh.validar_codigo("124h"))
        self.assertTrue(sh.validar_codigo("456"))
    def test_validar_saldo(self):
        self.assertTrue(sh.validar_saldo(5000))
        self.assertFalse(sh.validar_saldo(500000))
        self.assertTrue(sh.validar_saldo(1000))
    def tearDown(self) -> None:
        pass

if __name__=="__main__":
    unittest.main()