def find_uniq(arr):
    element = arr.pop()
    
    for x in arr:
        if x != element:
            return x
    return arr


print(find_uniq([1,1,1,1,2,1,1,1]))