"""
Trolls are attacking your comment section

A common way to deal with this situation is to remove all of the vowels from the trolls comments, neutralizing the
threat.

your task is to write a function that take a string and return a new string without vowels.

"""


def remove_vowels(str):
	vowels =["a","e","i","o","u","A","E","I","O","U"]
	new_str = str
	for v in vowels:
		new_str = new_str.replace(v,"")	
	return new_str



remove_vowels("This website is for losers LOL!!!")
