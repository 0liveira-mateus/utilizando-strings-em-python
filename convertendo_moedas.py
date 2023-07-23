class ExtraindoURL:
    def __init__(self, url):
        self.url = url
    def baseURL(self):
        separador_interrogacao = self.url.find('?')
        return (self.url[ :separador_interrogacao])
    def parametrosURL(self):
        separador_interrogacao = self.url.find('?')
        return (self.url[separador_interrogacao+1:])

    def extraindo_valor(self, valor):
        parametro_buscado = valor
        indice_do_parametro = self.parametrosURL().find(parametro_buscado)
        valor_final = indice_do_parametro + len(parametro_buscado) + 1
        impedidor = self.parametrosURL().find('&', indice_do_parametro)
        if impedidor == -1:
            return self.parametrosURL()[valor_final:]
        else:
            return self.parametrosURL()[valor_final:impedidor]

    def __str__(self):
        return f' A url possui como base = {self.baseURL()}, parametros = {self.parametrosURL()}'

    def convertendo_valores(self, moeda, valor_a_converter):
        if moeda == 'dolar':
            return f'valor em real é aproximadamente: {int(self.extraindo_valor(valor_a_converter)) * round(float(4.78))}'
        elif moeda == 'real':
            return f'valor em dolar é aproximadamente: {int(self.extraindo_valor(valor_a_converter)) / round(float(4.78))}'



youtube = ExtraindoURL('bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real')

print(youtube.convertendo_valores('real', 'quantidade'))