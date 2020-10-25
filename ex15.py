from sys import argv

script, file = argv

#First print
txt = open(file)
print(f"\nHere's your file {file}:\n")
print(txt.read())

#Second print
print("\nType another filename:")
file_two = input("-> ")
txt_two = open(file_two)
print(f"\nHere's your file {file_two}:\n")
print(txt_two.read())

#Third print
print("\nOne more time:")
file_three = input("-> ")
txt_three = open(file_three).read()
print(f"\nHere's your file {file_three}:\n")
print(txt_three)
