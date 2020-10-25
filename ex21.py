def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

print("\nLet's do some math with just functions!\n")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for the extra credit, type it in anyway.
print("\nHere is a puzzle:\n")

#age + {height - [weight * (iq / 2)]}
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("\nThat becomes: ", what, ". Can you do it by hand?\n")

#Formula
print("[(x + y - z) * x] / z")

print("x = ", end = "")
x = float(input())
print("y = ", end = "")
y = float(input())
print("z = ", end = "")
z = float(input())
print("")

resultado = divide(multiply(subtract(add(x, y), z), x), z)
print(f"\nTotal = {resultado}.\n")
