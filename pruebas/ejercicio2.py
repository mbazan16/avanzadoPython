import unittest

def esta_en_lista(elemento, lista):
    #if(edad<0): raise ValueError
    try:
        return True if elemento in lista else False
    except: #except BaseException
       return False  

class Ejercicio2Test(unittest.TestCase):
    lista=[1,2,3,4,5]
    
    
    def test_esta_en_lista(self):        
        self.assertEqual(esta_en_lista(2,self.lista),True)
        
    def test_no_esta_en_lista(self):        
        self.assertEqual(esta_en_lista(7,self.lista),False)
        
    def test_esta_en_list_sin_funcion(self):
        self.assertIn(2,self.lista)
        
    def test_esta_en_lista_lista(self):   
         
        self.assertEqual(esta_en_lista(7,None),False)



        
if __name__=="__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(PrueTestOtra))
    #unittest.TextTestRunner().run(suite)
    unittest.main(verbosity=2)