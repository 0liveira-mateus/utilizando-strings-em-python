url = "https://bytebank.com/cambio?moeda0rigem=real"

indice_interrogacao = url.find('?')
urL_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:44]

print(url)
print(urL_base)
print(url_parametros)
print(indice_interrogacao)