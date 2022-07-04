"""
@Auther-Sumit
@Goal-To take input and print * pattern

"""

num=int(input("enter number of row:"))

for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


"""
     *
    * *
   * * *
  * * * *
  """