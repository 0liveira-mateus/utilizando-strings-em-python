import re
class ExtratorURL:
    def __init__(self, url):
        self.url = url.strip()
        self.validaURL()

    def validaURL(self):
        padrao = re.compile('(http(s)?://)?(www.)?(bytebank.com)(.br)?(/cambio)?')
        match = padrao.match(self.url)

        if self.url == "":
            raise ValueError("A URL está vazia")
        elif not match:
            raise ValueError('URL INVÁLIDA')
        else:
            return ('URL válida')

    def urlBase(self):
        separador = self.url.find('?')
        url_base = self.url[0:separador]
        return url_base
    def urlParam(self):
        separador = self.url.find('?')
        url_parametros = self.url[separador+1:]
        return  url_parametros

    def valorParam(self, escritas):
        parametro_buscado = escritas
        indice_do_parametrobuscado = self.urlParam().find(parametro_buscado)
        valor_indice = indice_do_parametrobuscado + len(parametro_buscado) + 1
        separador_e = self.urlParam().find('&', indice_do_parametrobuscado)
        if separador_e == -1:
            final = self.urlParam()[valor_indice:]
        else:
            final = self.urlParam()[valor_indice:separador_e]
        print(final)


Alura = ExtratorURL('bytebank.com.br')

print(Alura.validaURL())