
"""
def solution(s):
    new_list = []
    if len(s) % 2 == 0:
        s += '_'
    for i in range(0, len(s), 2):
        new_list.append(s[i : i + 2])
    
    print(new_list)
    return new_list
    """
    
def split_pairs(a):
    new_lst = []

    if len(a) % 2 != 0:
        a += "_"

    for i in range(0, len(a), 2):
        new_lst.append(a[i : i + 2])
    return new_lst


print(split_pairs("abcd"))  # == ['ab', 'cd']
print(split_pairs("abc"))  # == ['ab', 'c_']
print(split_pairs("abcdf"))  # == ['ab', 'cd', 'f_']
print(split_pairs("a"))  # == ['a_']
print(split_pairs(""))  # == []
    
    
    
#solution("asdfec")
#solution("asdfc")