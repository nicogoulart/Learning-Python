from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read(), "\n")

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print(line_count, f.readline(), end = '')

def print_three(line_count, f):
	print_a_line(line_count, f)
	line_count += 1
	print_a_line(line_count, f)
	line_count += 1
	print_a_line(line_count, f)

def auto(line_count, f):
	print("\nFirst let's print the whole file:\n")
	print_all(f)
	print("Now let's rewind, kind of like a tape. \n")
	rewind(f)
	print("Let's print three lines:")
	print_three(line_count, f)
	print("")

current_line = 1
current_file = open(input_file)

auto(current_line, current_file)
