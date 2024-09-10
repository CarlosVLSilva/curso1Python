# Módulos padrão do Python (import, from, as e *)

# inteiro - import nome_modulo
#vantagens: vc tem o namespace do modulo
# Destvantagens: nomes grandes
# import sys

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: sem o namespace do modulo
"""from sys import exit, platform

print(platform)"""

# alias 1 - import nome_modulo as apelido
# import sys as s

# alias 2 - from nome_modulo import objeto as apelido
# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

#má prática - from nome_modulo import *
# Vantagem: importa tudo do módulo
# Desvantagem: importa tudop do módulo