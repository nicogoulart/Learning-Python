#É possível utilizar argumentos na linha de comando do Python3 utilizando a função argv do módulo sys (sys.argv).

from sys import argv
script, primeiro, segundo, terceiro = argv
#O primeiro argumento de argv é o próprio nome do arquivo que será executado (nesse caso, 6_argumentos_linha_comando.py). Os argumentos primeiro, segundo e terceiro são variáveis que você deve fornecer ao executar o script. Argumentos sempre serão interpretados como string.

print("\nO nome desse script é:", script)
print("A primeira variável que você forneceu:", primeiro)
print("A segunda variável que você forneceu:", segundo)
print("A terceira variável que você forneceu:", terceiro)

p = int(primeiro)
s = int(segundo)

print("\n\tSomar a primeira variável com a segunda:")
print(f"\t{p} + {s} = ", p + s, "\n")
