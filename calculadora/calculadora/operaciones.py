import logging

def suma(a,b):
    logger = logging.getLogger('root')
    logger.info(f'suma {a} + {b}')
    return a+b

def resta(a,b):
    logger = logging.getLogger('sampleLogger')
    logger.info(f'resta {a} - {b}')
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b