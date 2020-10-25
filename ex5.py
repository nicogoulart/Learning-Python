name = 'Nicolas Goulart'
age = 22
height = 1.68 #meters
weight = 55 #kilograms
centimeters = height * 100
grams = weight * 1000
eyes = 'Brown'
hair = 'Brown'
skin = 'White'

print(f"Let's talk about {name}.")
print(f"He's {height} meters tall.")
print(f"(That means {centimeters} centimeters)")
print(f"He's {weight} kilograms heavy.")
print(f"(That means {grams} grams)")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His skin is {skin}.")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}.")
