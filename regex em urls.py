import re

url = '/cambio'

padrao = re.compile('(http(s)?://)?(www.)?(bytebank.com)(.br)?(/cambio)')
match = padrao.match(url)

if not match:
    raise ValueError("A URL não é válida.")
else:
    print('Url Válida')