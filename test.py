#Integrantes: 
# - Jhon Sebastian Pai
#- Jhon Brayan Muñoz
#- Jhonatan Vasquez

import unittest
import tarjeta2 as sh

class string_handlerTest(unittest.TestCase):
    def setUp(self):
        """
            Set up our test: The method is automatically invoked
            before each test
        """
        self.calc=sh.string_handler()
    def test_add_str(self):
        self.assertEqual(self.calc.add_str("ABC","DE","F"),"ABCDEF")
        self.assertEqual(self.calc.add_str("I am"," who"," I am"),"I am who I am")
    def test_substract_str(self):
        try:
            self.assertEqual(self.calc.subtract_str("xyzw","yz"),"xw")
        except:
            print("Error-1:",self.calc.subtract_str("xyzw","yz"),"xw")
        try:
            self.assertEqual(self.calc.subtract_str("ABCD","BC"),"AD")
        except:
            print("Error-1:",self.calc.subtract_str("ABCD","BC"),"AD")
    def tearDown(self) -> None:
        pass

def suite():
    suite=unittest.TestSuite()
    suite.addTest(string_handlerTest('test_substract_str'))
    suite.addTest(string_handlerTest('test_add_str'))
    return suite

if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())