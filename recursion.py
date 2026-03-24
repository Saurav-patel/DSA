# def printNumbers(num):
#     if num > 50:
#         return
#     print(num)
#     num+=1
#     printNumbers(num)


# def printNto1(num):
#     if num < 1:
#         return
    
#     print(num)
#     printNto1(num-1)




# def evenNumbers(num):
#     if num >20:
#         return
#     if num % 2 == 0:
        
#         print(num)
#     num+=1
#     evenNumbers(num)

# def factorial(num):
#     if num < 1:
#         return 1
#     return num * factorial(num-1)

    
# def sumOfN(num):
#     if num < 1:
#         return 0
#     return num + sumOfN(num-1)



# def backTrack(i , num):
#     if i< 1:
#         return
#     backTrack(i-1 , num)
#     print(i)

# if __name__ == "__main__":
#     sum = 0
#     # num = 1
#     # printNumbers(num)
#     # print("Even numbers: less than 20")
#     # evenNumbers(num)
#     num = int(input("Enter a number to find factorial: "))
#     print("Factorial:", factorial(num))
#     printNto1(num)
#     print("Sum of first", num, "natural numbers:", sumOfN(num))
#     print("Backtracking from", num, "to 1:")
#     backTrack(num, num)

    
# arr = [1, 2, 3, 4, 5]

# def reverseArray(arr, start, end):
#     if start >= end:
#         return
#     arr[start],arr[end] = arr[end],arr[start]
#     reverseArray(arr,start+1,end-1)

# reverseArray(arr, 0, len(arr)-1)
# print("Reversed array:", arr)



# def checkPalindrome(s ):
#     check = s
#     def helper(check,left , right):
#         print("hello")
#         if left > right:
#             return
#         check[left],check[right] = check[right],check[left]
#         helper(check,left+1,right-1)
#     helper(check,0,len(check)-1)
#     if s == check:
#         return True
#     return False
    
# checkPalindrome("madam")

def isPalindrome(s):
    check = s
    def helper(left , right):
        if left >= right:
            return True
        if check[left] != check[right]:
            return False
        return helper(left+1,right-1)
    return helper(0,len(s)-1)

print(isPalindrome("madamc"))

# def checkPalindrome(s):
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if s[left ] != s[right]:
#             return False
#         left+=1
#         right-=1
#     return True

# print(checkPalindrome("madam"))


print(len("hello"))

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(3))
# print(fib(2))


def printFib(n):
    a = 0
    b = 1
    
    if n <= 0:
        return
    # for i in range(n):
    #   print(a,end=" ")
    #   a,b = b,a+b
    # upto n
    # while a < n:
    #     print(a,end=" ")
    #     a,b = b,a+b

    for i in range(n):
        if a >= n:
            break
        print(a,end=" ")
        a,b = b,a+b
printFib(10)


arr = [1, 2, 3, 4, 5]
end = len(arr)-1
for i in range(len(arr)-1):
    arr[i],arr[end] = arr[end],arr[i]
    end-=1

print(arr)

def reverseArray(arr, start, end):
    if start >= end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    reverseArray(arr,start+1,end-1)

reverseArray(arr, 0, len(arr)-1)
print("Reversed array:", arr)





        
