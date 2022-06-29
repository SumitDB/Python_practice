"""
Auther-Sumit
Goal-To print Fibonacci Series till 89 
Logic is next number = (n-1) + (n-2)"""


n1=0
n2=1
count=0
l1=[]
while count < 12:
    l1.append(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count= count+1

print(l1)
