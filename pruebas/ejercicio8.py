import unittest

def sumar_pares(numero=...):
    numero =int(numero)
    lista_numeros_pares =[num for num in range( numero+1) if num % 2 == 0]
    suma = sum(lista_numeros_pares)
    return suma
 


class Ejercicio8Test(unittest.TestCase):
  
    def test_sumar_pares(self):        
        self.assertEqual(sumar_pares(2),2)
        
    def test_sumar_pares_sin_pares(self):        
        self.assertEqual(sumar_pares(1),0)
    
    def test_sumar_pares_sin_pares(self):        
        self.assertEqual(sumar_pares('1000'),250500)
        
    def test_sumar_pares_cadena_numerica(self): 
      self.assertEqual(sumar_pares('2'),2)
    
    def test_sumar_pares_cadena_no_numerica_type_error(self): 
     with self.assertRaises(Exception):
         sumar_pares('a')
    
    def test_sumar_pares_nulo_value_error(self): 
     with self.assertRaises((ValueError,TypeError)):
         sumar_pares()


        
if __name__=="__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(PrueTestOtra))
    #unittest.TextTestRunner().run(suite)
    unittest.main(verbosity=2)