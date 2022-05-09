"""
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
"""


class vector:
    def __init__(self,vetor):
        self.vetor = vetor
        self.myList = []

    def addData(self, data):
        self.myList.append(data)

    def __getitem__(self, item):
        return getattr(self, item)
    
    def __len__(self,data):
        return len(self, data)
    
    def add(self,arr):
        array = self.vetor
        second_array = arr
        count = len(array)
        a = vector()
        for x in range(0, len(array)):
            a.addData(array[x] + second_array[x])
            
        print(a.myList)
        return 0
            

new = vector([1,2,3])
second = vector([4,5,6])

new.add(second)