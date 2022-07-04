"""
@Auther-Sumit
@Goal-To take input and print * pattern

"""

def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'* '*(i+1))




pyramid(5)