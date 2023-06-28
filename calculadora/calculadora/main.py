import logging
import logging.config
#from operaciones import suma,resta,multiplicar,dividir
import operaciones as op

if __name__ == '__main__':   
   logging.config.fileConfig('logging.conf')
   #logger = logging.getLogger('root')
   op.suma(2,3)
   op.resta(45,20)