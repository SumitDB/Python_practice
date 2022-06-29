"""
Auther-Sumit
Goal-To sort list without use of sort
"""

list1=[23,343,5,5,6,7,898,567,2345,234,76]
new_list=[]
while list1:
    minimum=list1[0]
    for x in list1:
        if minimum < x:
            minimum = x
    new_list.append(minimum)
    list1.remove(minimum)
print(new_list)
        