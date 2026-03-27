def arrayInput(arr,num):
    for i in range(num):
        element = int(input("Enter elements:"))
        arr.append(element)
    return arr

if __name__ == "__main__":
    # print("This is a module for hashing functions.")
    
    # num = int(input("Enter the number of element: "))
    # arr = []  
    # arrayInput(arr, num)

    # hash_arr = [0] * 12
    # for i in range(num):
    #     hash_arr[arr[i]] += 1


    # a = int(input("Enter the number to be hashed: "))
    # for i in range(a):
    #     number  = int(input("Enter the number to be hashed: "))
    #     print("Occurrences of", number, ":", hash_arr[number])


    # arr = [1, 2, 3, 4, 5 , 1,3 , 3]

    # hash_arr = [0] * 12
    # for i in range(len(arr)):
    #     hash_arr[arr[i]] += 1
    # print(hash_arr)

    # num = int(input("Enter the no. u want to find the count of"))
    # print("Occurance:", hash_arr[num])
    
    # def countFrequency(nums , number):
        
    #     hash_arr1 = [0] * 12
    #     for i in range(len(nums)):
    #         hash_arr1[nums[i]] += 1
        
    #     twoDArray = []
    #     for i in range(len(hash_arr1)):
    #         if hash_arr1[i] > 0:
    #             twoDArray.append([i,hash_arr1[i]])
        
    #     print(twoDArray)
    # nums = [1,3,2,4,5,6 , 1,3,3,2]
    # countFrequency(nums ,3)
    
    arr = [12,3,4,3,2,1,2,3,4]
    hash_arr = [0] * 13
    for i in arr:
        hash_arr[i]+=1
    

    # for i in range(len(hash_arr)):
    #     if hash_arr[i] > 0:
    #         print(i , "Appears" , hash_arr[i] , "times")
    
    # def countOccurance(s,c):
    #     hash_arr1 = [0] * 256

    #     for i in s:
    #         hash_arr1[ord(i)]+=1
    #     twoDArray = []
    #     for i in c:
    #         print(i , hash_arr1[ord(i)])
    #         twoDArray.append([i,hash_arr1[ord(i)]])
    #     print(twoDArray)

        
    # s = input("Enter the string :")
    # num = int(input("Enter the no. of character u want to enter :"))
    # c = []
    # for i in range(num):
    #     chr = input("Enter the character :")
    #     c.append(chr)
    # countOccurance(s,c)

    def countOccurance(nums):
        hash_arr =  [0] * 7
        for i in nums:
            hash_arr[i] += 1
        maxx = hash_arr[0]
        element = 0
        for i in range(len(hash_arr)):
            if hash_arr[i] > maxx:
                maxx = hash_arr[i]
                element = i
        print(element)

        
    def leastOccurance(nums):
        hash_arr = [0] * 10
        for i in nums:
            hash_arr[i]+=1
        minn = float('inf')
        print(hash_arr)
        print(minn)
        element = 0
        for i in range(len(hash_arr)):
            if hash_arr[i] > 0 and hash_arr[i] < minn:
                minn = hash_arr[i]
                element = i
        print("element : " , element , "Frequency : ",minn )

            
            
    def elementsNumber(nums):
        twoDArray = []
        hash_arr = [0] * 10
        for i in nums:
            hash_arr[i] += 1

        for i in range(len(hash_arr)):
            if hash_arr[i] > 0:
                twoDArray.append([i , hash_arr[i]])
        print(twoDArray) 
    arr = [4,4,5,5,6]
    countOccurance(arr)
    leastOccurance(arr)
    elementsNumber(arr)