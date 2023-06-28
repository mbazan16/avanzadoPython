import unittest

def dividir(a, b):
    return a/b
    

class Ejercicio3Test(unittest.TestCase):
  
    def test_dividir_2_2(self):        
        self.assertEqual(dividir(4, 2),2)
        
    def test_dividir_10_3(self):        
        self.assertAlmostEqual(dividir(10, 3),3.33,places=2) #places=2 el numero de decimales que compara
        
    def test_dividir_x_0(self): 
     with self.assertRaises(ZeroDivisionError):
         dividir(10, 0)


        
if __name__=="__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(PrueTestOtra))
    #unittest.TextTestRunner().run(suite)
    unittest.main(verbosity=2)