from bs4 import BeautifulSoup

class ParseoHelper(object):
    """description of class"""
    @staticmethod
    def ObtenerElementos(contenidoHtml, listaElementos):
        return contenidoHtml.find_all(listaElementos)
   

