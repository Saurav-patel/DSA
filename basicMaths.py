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
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    return num == sum

print("Is Armstrong:", isArmstrong(num))