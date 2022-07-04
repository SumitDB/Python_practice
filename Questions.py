"""
Author-Sumit 
Goal-6 Interview questions
"""


"""
#Question1

number=[5,7,5,5,5,7,7,5]

number.sort()
print(number)

"""
"""
#Question2
input =  [1,2,'A',8,'G',3,'X','M',9]
new_list=[]
len=len(str(input))
for i in range (len):
    new_list.insert(i,input[-1])
print(a)
"""

"""
#Question3
input ='I!am!a!coder'
output=" ".join(reversed(input.split("!")))
print(output)
"""
"""
#Question4
a=[2,0,3,3,4,4,5]
output=[0,]
ele_count={}
for element in a:
    if element in ele_count:
        ele_count[element]+=1
    else:
        ele_count[element]=1
for key,value in ele_count.items():
    output.append(value)
print(output)

"""
"""
#Question5
k =3
Arr=[7,6,1,2,4,5]
new_list=[]

Arr.sort()
output=Arr[3]
print(output)
"""


"""
#Question6
n1={"a1":10,"b2":20,"c3":30}
key1="a1"
key2="b2"
key3="c3"
n1[key1]= n1.get(key1,0)+1
n1[key2]= n1.get(key2,0)+1
n1[key3]= n1.get(key3,0)+1
print(n1)
"""