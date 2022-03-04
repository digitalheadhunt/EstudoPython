def move_zeros(arr):
    
    for element, index in arr:
        if element == 0:
            iszero = arr.pop(index)
            arr.append(iszero)
    
    return arr

print(move_zeros([1,0,2,0,0,3,4,2]))