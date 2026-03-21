def printNumbers(num):
    if num > 50:
        return
    print(num)
    num+=1
    printNumbers(num)


def printNto1(num):
    if num < 1:
        return
    
    print(num)
    printNto1(num-1)




def evenNumbers(num):
    if num >20:
        return
    if num % 2 == 0:
        
        print(num)
    num+=1
    evenNumbers(num)

def factorial(num):
    if num < 1:
        return 1
    return num * factorial(num-1)

    
def sumOfN(num):
    if num < 1:
        return 0
    return num + sumOfN(num-1)
if __name__ == "__main__":

    # num = 1
    # printNumbers(num)
    # print("Even numbers: less than 20")
    # evenNumbers(num)
    num = int(input("Enter a number to find factorial: "))
    print("Factorial:", factorial(num))
    printNto1(num)
    print("Sum of first", num, "natural numbers:", sumOfN(num))

    
