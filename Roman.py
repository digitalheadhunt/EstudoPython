"""
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

"""

def solution(roman):
    new_value = 0; 
    for number in roman:
        if number == "I":
            new_value += 1
        elif number == "V":
            new_value += 5
        elif number == "X":
            new_value += 10
        elif number == "L":
            new_value += 50
        elif number == "C":
            new_value += 100
        elif number == "D":
            new_value += 500
        elif number == "M":
            new_value += 1000
    return new_value

print(solution("MMIX"))
