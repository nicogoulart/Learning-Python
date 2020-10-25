class mystuff(object):
	def __init__(self):
		self.tangerine = "And now a thousand years between"

	def apple(self):
		print("I AM CLASSY APPLES!")

class song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

thing = mystuff()
thing.apple()
print(thing.tangerine)

birthday_song = ["Happy birthday to you",
		"I don't want to get sued",
		"So I'll stop right there."]

other_song = ["They rally around the family",
		"With pockets full of shells."]

happy_bday = song(birthday_song)
bulls_on_parade = song(other_song)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
