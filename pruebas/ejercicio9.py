import unittest
import logging

def ordenar_lista(lista:list[str]) -> list[str]:
      lista_minusculas=[x.lower() for x in lista]
      lista_ordenada=sorted(lista_minusculas)
      return lista_ordenada
 
class MiObjeto:
    def __init__(self,nombre):
        self.nombre=nombre
    def __eq__(self,obj):
        return self.nombre==obj.nombre
    def __str__(self):
        return f'MiObjeto[nombre={self.nombre}]'
        

def mifuncion():
    return MiObjeto('Maria')
    
    




class Ejercicio9Test(unittest.TestCase):    
     
    lista=['HOLA', 'Pepe', 'ALBa', 'AdiOS', 'viva', 'MADRID']
    lista_ordenada=['adios', 'alba', 'hola', 'madrid', 'pepe', 'viva']
    objeto = MiObjeto('Maria')
    def test_1(self): 
        logging.basicConfig(level=logging.DEBUG, filename="misTrazas.log",format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info('{Ejercicio9Test}-{test_1}') 
        #self.assertEqual(id(ordenar_lista(self.lista)),id(self.lista_ordenada))
        logging.debug(MiObjeto('Pepe'))
        self.assertEqual(mifuncion(),self.objeto)
        
    

        
if __name__=="__main__":
    #suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(PrueTestOtra))
    #unittest.TextTestRunner().run(suite)
    unittest.main(verbosity=2)