import unittest

def es_mayor_de_edad(edad):
    #if(edad<0): raise ValueError
    return True if edad>=18 else False

class Ejercicio1Test(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        self.assertEqual(es_mayor_de_edad(20),True)
    
    def test_es_18_de_edad(self):
        self.assertEqual(es_mayor_de_edad(18),True)
    
    def test_es_menor_de_edad(self):
        self.assertEqual(es_mayor_de_edad(15),False)
 
    def test_es_negativo_de_edad(self):
        self.assertEqual(es_mayor_de_edad(-5),False)
        
    def test_es_tipo_cadena(self):
        with self.assertRaises(TypeError):
            es_mayor_de_edad('a')
    def test_es_vacio_edad(self):
        with self.assertRaises(TypeError):
            es_mayor_de_edad()
    def test_es_nulo_edad(self):
        with self.assertRaises(TypeError):
            es_mayor_de_edad(None)
    def test_es_espacio_valor_edad(self):
        self.assertEqual(es_mayor_de_edad( 5),False)



        
if __name__=="__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(PrueTestOtra))
    #unittest.TextTestRunner().run(suite)
    unittest.main(verbosity=2)