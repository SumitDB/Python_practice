"""
Author-Sumit
Goal-To check the given number is Palindrome or not
"""


num=int(input("Enter a number"))

temp=num
rev=0
while temp>0:
    digit=temp%10
    rev= rev*10+digit
    temp //=10

if rev==num:
    print(num,"is Palindrome")
else:
    print(num," is not a palindrome")
