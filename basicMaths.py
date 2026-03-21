def SumOfDigits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    return sum


num = int(input("Enter a number: "))
print("Sum of digits:", SumOfDigits(num))

def countDigits(num):
    count = 0
    # for i in str(num):
    #     count = count + 1
    while num > 0:
        count += 1
        num = num // 10
    return count


print("Number of digits:", countDigits(num))


def reverseNum(num):
    reverseNum = 0
    while num > 0:
        digit = num % 10
        reverseNum = reverseNum * 10 + digit
        num = num // 10
    return reverseNum

print("Reversed number:", reverseNum(num))


def isPalindrome(num):
    reverseNum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reverseNum = reverseNum * 10 + digit
        temp = temp // 10
    return num == reverseNum

print("Is palindrome:", isPalindrome(num))


def isArmstrong(num):
    sum =  0
    temp = num
    pow = 0
    while temp > 0:
        digit = temp % 10
        pow += 1
        temp = temp // 10
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** pow
        temp = temp // 10
    return num == sum


print("Is Armstrong:", isArmstrong(num))


def printDivisors(num):
    divisor = []
    n = 1
    while n <= num:
        if num % n == 0:
            divisor.append(n)
        n+=1
    return divisor

print("Divisors:", printDivisors(num))


def isPrime(num):
    n = 2
    while n < num:
        if num % n == 0:
            return False
        n+=1
    return True

print("Is prime:", isPrime(num))

def printPrime(num1, num2):
    primes = []

    for i in range(num1, num2 + 1):
        if i < 2:
            continue

        is_prime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


print("Prime numbers between", num1, "and", num2, "are:", printPrime(num1, num2))