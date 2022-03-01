#first we need create a function 
# this function will receive a integer
# and will return a integer 

import math
import timeit

def returnsquare (vlr):
    if vlr < 0:
        return False
    else:
         
       raiz = math.sqrt(vlr)
    
    return raiz


returnsquare(10)

print(timeit(returnsquare(25)))