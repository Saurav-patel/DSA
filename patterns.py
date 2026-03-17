#first pattern
# *****
# *****
# *****
# *****
# *****
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()

n = int(input("Enter the number of rows: "))
#pattern1(n)


#second pattern
# *
# **
# ***
# ****
# *****

def pattern2(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*" , end="")
        print()

#pattern2(n)


#third pattern
# 1
# 12
# 123
# 1234
# 12345

def pattern3(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j , end="")
        print()

#pattern3(n)

#fourth pattern
# 1
# 22
# 333
# 4444
# 55555

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i , end="")
        print()

#pattern4(n)

#fifth pattern
# *****
# ****
# ***
# **
# *

def pattern5(n):
    for i in range(1,n+1):
        for j in range(n , i-1 , -1):
            print("*" , end="")
        print()

#pattern5(n)


#pattern 6
# 12345
# 1234
# 123
# 12
# 1

def pattern6(n):
    for i in range(n , 0 , -1):
        for j in range(1 , i+1):
            print(j , end="")
        print()

#pattern6(n)

#pattern 7
#     *
#    ***
#   *****
#  *******
# *********

def pattern7(n):
    for i in range(1,n+1):
        for j in range(n , i-1 , -1):
            print(" " , end="")
        for k in range(1 , 2*i):
            print("*" , end="")
        print()
pattern7(n)
