url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

indice_interrogacao = url.find('?')
urL_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]


var1 = 'moedaOrigem'
buscar = url_parametros.find(var1)

print(buscar)

achando = url_parametros[buscar + len(var1) + 1:]
print(achando)


var2 = 'moedaDestino'
buscar2 = url_parametros.find(var2)

print(buscar2)

indice_E = url_parametros.find('&')
achando2 = url_parametros[buscar2 + len(var2) + 1: indice_E]
print(achando2)