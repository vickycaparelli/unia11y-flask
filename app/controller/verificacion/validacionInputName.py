import re
from bs4 import BeautifulSoup
from app.controller.resultadocriterio import ResultadoCriterio

class validacionInputName(object):
    """ Realiza la verificacion del Criterio 1
         -  Input Name """

    @staticmethod
    def Verificar(elementos, idregla, reglas):

        elementosInvalidos = list()

        contador = 0
        # Valido que los input tengan atributo name y este tenga una longitud mayor a 3
        for elemento in elementos:
            elemento_str=str(elemento)
            name= re.findall(r'name="([0-9a-zA-Z_]+)"',elemento_str)
            if len(name)==0:
                elementosInvalidos.append(elemento)
                contador+=1
            elif len(name[0])<3:
                elementosInvalidos.append(elemento)
                contador+=1

        return ResultadoCriterio(idregla, reglas[idregla][0],reglas[idregla][1], elementosInvalidos, reglas[idregla][4])
