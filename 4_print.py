var1 = 10
var2 = 8.55
var3 = 'a'
var4 = 'nicolas'

#Imprimindo algo na tela.
print("Isto é uma string que irá ser impressa na tela.\n")

#Colocando uma variável entre strings (separadas por vírgula) é possível chamar a variável e a imprimir na tela.
print("A variável var1 =", var1, "foi impressa na tela, e a variável var2 =", var2, "também.\n")

#Colocando f (de format) antes de uma string para ser impressa é possível colocar o valor de variáveis dentro de colchetes.
print(f"var1 = {var1}, var2 = {var2}, var3 = {var3}, var4 = {var4}.")

#A função format() funciona de igual forma.
print("var1 = {}, var2 = {}, var3 = {}, var4 = {}.\n".format(var1, var2, var3, var4))
print("Eu gosto de {}.\n".format('pizza'))

nome = 'Nicolas Goulart'
nascimento = 1995
altura = 1.68
peso = 55

#É possível criar variáveis com strings já formatadas, e depois as imprimir.
a = f"Meu nome é {nome}."
b = f"Nasci no ano de {nascimento}."
c = f"Tenho {altura} metros de altura."
d = f"Peso {peso} quilogramas.\n"

print(a)
print(b)
print(c)
print(d)

print(f"Recapitulando: {a} {b} {c} {d}")

#É possível criar strings com formatação vazia e então preencher utilizando a função format().
pergunta_nome = "Qual o meu nome? {}"
pergunta_nascimento = "Qual o meu ano de nascimento? {}" 
pergunta_altura = "Qual a minha altura? {}"
pergunta_peso = "Qual o meu peso? {}\n"

print(pergunta_nome.format(nome))
print(pergunta_nascimento.format(nascimento))
print(pergunta_altura.format(altura))
print(pergunta_peso.format(peso))

outra_pergunta = "Porque a galinha atravessou a rua? {}"
resposta = "Para chegar ao outro lado.\n"
impressao = outra_pergunta.format(resposta)
print(impressao)

vazio = "{} {} {} {}"
print(vazio.format('um','dois','três','quatro'))
print(vazio.format('Cabeça,','ombro,','joelho e','pé!'))
print(vazio.format(True, False, True, False))
print(vazio.format(10, 20, 30, 40))
print(vazio.format(vazio, vazio, vazio, vazio), "\n")

esquerdo = "Esse é o lado esquerdo..."
direito = "de uma string com um lado direito.\n"
print(esquerdo + direito) #Imprime duas strings juntas, uma ao lado da outra.

letra1 = "C"
letra2 = "h"
letra3 = "e"
letra4 = "e"
letra5 = "s"
letra6 = "e"
letra7 = "B"
letra8 = "u"
letra9 = "r"
letra10 = "g"
letra11 = "e"
letra12 = "r"

#A variável "end" após a vírgula substitui a quebra de linha por outra string ao final de uma impressão.
#Nesse caso, colocamos apenas um espaço em branco para separar as duas palavras. 
print(letra1 + letra2 + letra3 + letra4 + letra5 + letra6, end = ' ')
print(letra7 + letra8 + letra9 + letra10 + letra11 + letra12, "\n")

#Utilizando três aspas em um print é possível reconhecer as quebras de linha.
print("""Era uma vez um glorioso guerreiro.
Um belo dia ele tropeçou em uma pedra.
Bateu de cabeça no chão e morreu.
Fim! :)\n""")

print("*" * 10) #Multiplica a impressão de uma mesma string.

#O \n é utilizado para quebrar a linha.
print("\nEsse texto está \ndividido em duas linhas.\n")

#O \t é utilizado para dar tab.
print("Tab! \tOh, não...")

#O \\ ou \" e \' são utilizados para imprimir esses caracteres que geralmente são utilizados para outros propósitos dentro do print.
print("Testemunhe: \\, \', e \"! Muahaha Ò__Ò\n")

#O comando input() recebe o valor que você fornecer na tela e o transfere para a variável.
#Lembre-se que o valor fornecido será entendido como uma string, então é preciso converter para outros dados. Também é possível utilizar a função eval() para converter automaticamente a string recebido para uma expressão reconhecido por Python.
print("Testando a função input() com conversão. Forneça um número:", end= ' ')
n1 = input()

print("Testando a função input() com conversão. Forneça outra número:", end = ' ')
n2 = input()

numero1 = int(n1)
numero2 = int(n2)

print("Eis a soma desses números após conversão: ", numero1 + numero2)
print("Perceba como fica a soma dos números sem a conversão (interpretados como strings):", n1 + n2)

print("\nAgora vamos utilizar a função eval() no input. Forneça um número:", end= ' ')
ne1 = eval(input())

print("Agora vamos utilizar a função eval() no input. Forneça outro número:", end= ' ')
ne2 = eval(input())

print("Eis a soma dos números: ", ne1 + ne2)

#É possível utilizar uma string dentro de input.
print("\nOlá, como vai?")
estado = input('-> ')

print(f"Então você está {estado}. Que legal!\n")

nome = input("Qual o seu nome? -> ")
nascimento = input("Em que ano nasceu? -> ")
print(f"Seja bem-vindo ao Python3, meu caro {nome} do ano {nascimento}!\n")
