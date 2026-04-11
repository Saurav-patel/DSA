
def findNumApperanceOnce(nums):
    # optimal approach: Using XOR operator
    xor_result = 0
    # xor_result = 0
    # for i in range(len(nums)):
    #     xor_result^= nums[i]
    # return xor_result

    # # Approach 2 better: Using Hash Map
    # hash_mqp = [0] * 10
    # for i in range(len(nums)):
    #     hash_mqp[nums[i]]+=1
    # for i in range(len(hash_mqp)):
    #     if hash_mqp[i] == 1:
    

    

    # brute force approach
    # for i in range(len(nums)):
    #     num = nums[i]
    #     count = 0
    #     for j in range(i+1,len(nums)):
    #         if nums[j] == num:
    #             count +=1
    #     if count == 1:
    #         return num

def findUnique(nums):
    low = 0
    high = 1
    
    for high in range(len(nums)):
        if nums[low] != nums[high]:
            low += 1
            nums[low] = nums[high]
    return nums[:low]            

def squareOfSortedArray(nums):
    low = 0
    high = len(nums) - 1
    temp = [0] * len(nums)
    while low <= high:
        if nums[low]**2 > nums[high]**2:
            temp[high-low] = nums[low]**2
            low += 1
        else:
            temp[high-low] = nums[high]**2
            high -= 1
    return temp

if __name__ == "__main__":
    arr = [1,1,3,4,5,5,3]
    arr2 = [-4,-1,0,3,10]
    print(squareOfSortedArray(arr2))
    # print(targetSumSubArray(arr, 5))
    # # print(findNumApperanceOnce(arr))
    # print(targetSumSubArrayBetter(arr, 5))
    # d = {}
    # target = 5
    # for i,j in enumerate(arr):
    #     if target - j in d:
    #         print(f"Pair found: ({j}, {target - j})")
    #         print(f"Pair found at index from {d[target-j]} to {i}")
    #     d[j] = i
    # print(d)
    print(findUnique(arr))