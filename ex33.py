def lista_numeros(cont, numeros, soma):
	while cont < numeros:
		print(f"At the top cont is {cont}.")
		numbers.append(cont)

		cont += soma

		print("Numbers now: ", numbers)
		print(f"At the bottom cont is {cont}.")

i = 0
numbers = []

tamanho = int(input("--> numeros = "))
add = int(input("--> somador = "))
lista_numeros(i, tamanho, add)

print("The numbers:")

for num in numbers:
	print(num)
