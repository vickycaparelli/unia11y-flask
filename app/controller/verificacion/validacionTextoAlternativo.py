import re
from bs4 import BeautifulSoup
from app.controller.resultadocriterio import ResultadoCriterio

class validacionTextoAlternativo(object):
    """ Realiza la verificacion del Criterio 1
         -  Textos Alternativos """

    @staticmethod
    def Verificar(elementos, idregla, reglas):

        elementosInvalidos = list()

        contador = 0
        # Valido que el atributo alt exista y tenga una longitud mayor a 3 digitos
        for elemento in elementos:
            elemento_str=str(elemento)
            alt= re.findall(r'alt="([0-9a-zA-Z_]+)"',elemento_str)
            print(elemento,alt)
            if len(alt)==0:
                elementosInvalidos.append(elemento)
                contador+=1
            elif len(alt[0])<3:
                elementosInvalidos.append(elemento)
                contador+=1

        return ResultadoCriterio(idregla, reglas[idregla][0],reglas[idregla][1], elementosInvalidos, reglas[idregla][4])
