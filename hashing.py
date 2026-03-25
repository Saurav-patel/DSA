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
    
    def countFrequency(nums , number):
        
        hash_arr1 = [0] * 12
        for i in range(len(nums)):
            hash_arr1[nums[i]] += 1
        
        twoDArray = []
        for i in range(len(hash_arr1)):
            if hash_arr1[i] > 0:
                twoDArray.append([i,hash_arr1[i]])
        
        print(twoDArray)
    nums = [1,3,2,4,5,6 , 1,3,3,2]
    countFrequency(nums ,3)
    