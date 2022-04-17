"""
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""


def rgb_hex(r,g,b):
    result = ''
    
    result += "%02x%02x%02x" % (r,g,b)
    
    return result.upper()

print(rgb_hex(255,158,144))