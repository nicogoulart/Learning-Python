print("""\nYou enter a dark room with two doors.
Do you go through door #1 or door #2 ?""")

door = input("--> door # ")

if door == "1":
	print("""\nThere's a giant bear here eating a cheese cake.
What do you do?

1. Take the cake.
2. Scream at the bear. """)
	
	bear = input("--> bear # ")
	
	if bear == "1":
		print("\nThe bear eats your face off. Good job!\n")
	
	elif bear == "2":
		print("\nThe bear eats your legs off. Good job!\n")

	else:
		print(f"""\nWell, doing {bear} is probably better.
Bear runs away.\n""")

elif door == "2":
	print("""\nYou stare into the endless abyss at Cthulhu's retina.
1. Blueberries.
2. Yellow jacket clothespins.
3. Understanding revolvers yelling melodies.""")

	insanity = input("--> insanity # ")

	if insanity == "1" or insanity == "2":
		print("\nYou body survives powered by a mind of jello. Good job!\n")

	else:
		print("\nThe insanity rots your eyes into a pool of muck. Good job!\n")

else:
	print("\nYou stumble around and fall on a knife and die. Good job!\n")
