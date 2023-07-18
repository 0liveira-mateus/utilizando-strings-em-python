endereco = 'Rua das flores 72, apartamento 1002, Laranjeiras, Rio de janeiro, RJ, 23440120'

import re  #Expressões Regulares -- RegEX

# 5 digitos = hifen (opconal) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # search servindo para saber se dentro de endereço tem algo com esse padrão

if busca:
    cep = busca.group()
    print(cep)