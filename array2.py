
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

def targetSumTriplets(nums,target):
    low = 0                                     # O(n^2) time complexity 
                                                #keep low fixed and move mid and high pointer to find the target sum 
    temp = [] 
    for low in range(len(nums)-2):
        
        high = len(nums) - 1
        mid = low+1 
        if low > 0 and nums[low] == nums[low-1]: # skip duplicates
            continue
        while mid < high:
            if nums[low] + nums[mid] + nums[high] == target:
                temp.append([nums[low], nums[mid], nums[high]])
                mid += 1
                high -= 1       
                # return (nums[low], nums[mid], nums[high])
                while mid < high and nums[mid] == nums[mid-1]: # skip duplicates
                    mid += 1
                while mid < high and nums[high] == nums[high+1]: # skip duplicates
                    high -= 1
            elif nums[low] + nums[mid] + nums[high] < target:
                mid += 1
                
            else:
                high -= 1
            
    return temp


def tripletSumClosest(nums , target):
    close = float("inf")
    temp = []
    for low in range(len(nums)-2):
        if low > 0 and nums[low] == nums[low-1]:
            continue
    
    
        left,right = low+1,len(nums)-1
        while left < right:
            sum = nums[low]+nums[left]+nums[right]
            if abs(target - sum) < abs(target - close):
                close = sum
                temp = ([nums[low], nums[left], nums[right]])
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return temp
    # return temp

if __name__ == "__main__":
    arr = [2,1,3,4,5,5,3]
    arr2 = [-4,-1,0,3,10]
    # print(squareOfSortedArray(arr2))
    print(targetSumTriplets(arr, 13))
    print(tripletSumClosest(arr,13))
    # print(targetSumTriplets(arr, 5))
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
    # print(findUnique(arr))