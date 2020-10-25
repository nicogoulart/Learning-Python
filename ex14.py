from sys import argv
script, username = argv

prompt = '-> '

print(f"\nHi {username}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(f"\nDo you like me, {username}?")
likes = input(prompt)

print(f"\nWhere do you live {username}?")
lives = input(prompt)

print("\nWhat kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said \"{likes}\" about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
