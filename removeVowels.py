"""

MY first solution

def remove_vowels(string_):
	vowels = ["a","e","i","o","u"]
	str_without_vowels = string_
	for v in vowels:
		str_without_vowels = str_without_vowels.replace(v,'')
	print(str_without_vowels)	
	return str_without_vowels



text1 = "The Trolls are Here"
text2 = "look
"""
def disemvowel(string_):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    str = string_
    
    for v in vowels:
        str = str.replace(v,'')
    return str

remove_vowels(text1)
remove_vowels(text2)				