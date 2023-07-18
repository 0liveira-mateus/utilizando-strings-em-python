##url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
url = ''

#Sanitização da UrL
url = url.strip()


#Validação da URL
if url == '':
    raise ValueError('A Url não pode ser vazia')


#Separando Url
separador = url.find('?')
url_base = url[0: separador]
url_parametros = url[separador+1:]


#Encontrando valores da Url
parametro_buscado = 'moedaOrigem'
indice_do_parametrobuscado = url_parametros.find(parametro_buscado)
indice_valor = indice_do_parametrobuscado + len(parametro_buscado) + 1
separador_e = url_parametros.find('&', indice_valor)
if separador_e == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:separador_e]
print(f'{parametro_buscado} :', valor)