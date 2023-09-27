import unittest
from nose2.tools import params
##from stringHandler import string_handler

def removeVowels(texto):
    vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    texto2 = ""
    for letra in texto:
        if letra not in vocales:
            texto2 += letra
    return texto2

class Test(unittest.TestCase):
    @params(("plato", "plt"),("pollo","pll"),("perro","prr"),("avion","vn"))
    def test_removeVowels(self,int,exp):
        self.assertEqual(removeVowels(int),exp)

if __name__ == "__main__":
    import nose2 
    nose2.main()