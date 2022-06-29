"""
Author- Sumit 
Goal-To Practice map function
"""



def add_function(n):
    return n*3

list1=(1,3,5,6,7,8,9)

list2= map(add_function,list1)

print(list(list2))
