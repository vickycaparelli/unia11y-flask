from bs4 import BeautifulSoup
from app.controller.resultadocriterio import ResultadoCriterio

class VerificacionCriterio01(object):
    """ Realiza la verificacion del Criterio 1
         -  Textos Alternativos """

    @staticmethod
    def Verificar(elementos, idregla, reglas):

        elementosInvalidos = list()

        contador = 0
        # Textos alternativos
        for elemento in elementos:
            try:
                aux = elemento[reglas[idregla][1]]
            except:
                aux = None
            elementosInvalidos.append(elemento)
            contador+=1
        return ResultadoCriterio(idregla, reglas[idregla][0], elementosInvalidos)
