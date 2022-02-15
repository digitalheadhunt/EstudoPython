"""
study list comprehension in python
 
 we can do a new list using the elements of a existent list, doing a expression in a 
 list to create a new list:

 	lista = [1,1,2,3,3,3,4,4,4,4,5,5,5,5,6]

 	new_list = [x for x in lista if x not in new_list]

"""

lista = [1,1,2,2,3,3,4,4,5,5,5,6,6,7]



new_list =[x * 2 for x in lista]

s = [x for x in lista if x % 2 == 0]

numbers = [x**2 for x in range(0,101)]
print(numbers)


dna = "AATTCG"

new_dna = []