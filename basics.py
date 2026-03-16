# class Solution:
#     def printNumber():
#         num = 7
#         print(num)

# Solution.printNumber()


# def printNames():
#     name = input("Enter your name: ")
#     print("Hello, " + name + "!")

# printNames()


# def addNumbers(a , b):
#     print(a + b)

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# addNumbers(num1, num2)

# num = int(input("Enter a number:"))

# def fun(num):
#     sq = num**2
#     return sq

# print("Square of the given number is ",fun(num))

# num1= int(input("Enter number 1:"))
# num2=int(input("Enter number2"))
# def sum(num1 , num2):
#     result = num1+num2
#     return result

# print("Sum = ",sum(num1,num2))




# cube = lambda x: x**3
# square = lambda num1,num2:num1**num2
# num1 = int(input())
# num2 = int(input())
# print(square(num1,num2))
# print(cube(2))

# def sum_all(*args):
#     return sum(args)
#     return sum

# print(sum_all(1,2))
# print(sum_all(1,2,3))

#want to make dictonaries of unknown number of items

# def kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# kwargs(name="Saurav" ,lname="Patel")

# def even_num(limit):
#     even=[]
#     for i in range(1,limit+1):
#         if(i%2==0):
#             even.append(i)
#     return even
        
# print(even_num(10))

#     #OR   By Yield

# def even_all(limit):
#     for i in range(0,limit+1,2):
#         yield i
    
# for num in even_all(10):
#     print(num)


#Recursion

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n * fact(n-1)
    
# n = int(input("Enter a number"))
# print(fact(n))



# def resultchecker(score):
#     if score > 100 or score < 0:
#         return "Invalid score"
#     if score >= 90 and score <= 100:
#         return "Grade A"
#     elif score >= 80 and score < 90:
#         return "Grade B"
#     else:
#         return "Grade C"
    
# score = int(input("Enter your score: "))
# print(resultchecker(score))


def printingEven(num1 , num2):
    if num1 % 2 != 0:
        num1 += 1
    for i in range(num1,num2+1 , 2):
        print(i)
num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))

printingEven(num1,num2)