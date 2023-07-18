url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

indice_interrogacao = url.find('?')
urL_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]


var1 = 'moedaDestino'
buscando = url_parametros.find(var1)
achando = buscando + len(var1) + 1


print(achando)

indice_e_comerial = url_parametros.find('&', achando)
if indice_e_comerial == -1:
    valor = url_parametros[achando:]
else:
    valor = url_parametros[achando:indice_e_comerial]

print(valor)

