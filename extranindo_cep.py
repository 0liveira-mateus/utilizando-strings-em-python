endereco = 'Rua das flores 72, apartamento 1002, Laranjeiras, Rio de janeiro, RJ, 23440-120'

import re  #Expressões Regulares -- RegEX

# 5 digitos = hifen (opconal) + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)