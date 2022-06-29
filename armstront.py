"""
Author- Sumit 
Goal-To find armstrong number
"""

num=int(input("Enter a number:"))

temp=num

armnum=0
leng= len(str(num))

while temp >0:
    digit= temp%10
    armnum= armnum + digit**leng
    temp//=10
if num==armnum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an arrmstrong number")