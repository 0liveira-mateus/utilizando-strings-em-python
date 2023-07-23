import re

url = 'http://Alura.com.br'

separador_interrogacao = url.find('?')
URL_base = url[:separador_interrogacao]
URL_parametros = url[separador_interrogacao+1:]

print(URL_base)
print(URL_parametros)

achar_parametro = 'moedaDestino'

posi_parametro = URL_parametros.find(achar_parametro)

print(posi_parametro)

result_parametro = posi_parametro + len(achar_parametro)+1




#--------------------------------------------------------------------------------------------------------------------

separador_e = URL_parametros.find('&', result_parametro)

if separador_e == -1:
    resultado_final = URL_parametros[result_parametro:]
    print(resultado_final)
else:
    resultado_final = URL_parametros[result_parametro:separador_e]
    print(resultado_final)


#--------------------------------------------------------------------------------------------------------------------

padrao = re.compile('(http(s)?://)?(Alura)(.com)(.br)?')
validar = padrao.search(url)

if validar :
    print('Url Válida')
else:
    print('Url Inválida')
