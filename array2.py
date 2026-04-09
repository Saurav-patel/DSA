
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
    #         return i


    # brute force approach
    # for i in range(len(nums)):
    #     num = nums[i]
    #     count = 0
    #     for j in range(i+1,len(nums)):
    #         if nums[j] == num:
    #             count +=1
    #     if count == 1:
    #         return num

def targetSumSubArray(nums , target):
    max_length = 0
    for i in range(len(nums)):
        sum = 0
        
        temp = []
        for j in range(i,len(nums)):
            
            sum += nums[j]
            print("sum =", sum)
            temp.append(nums[j])
            if sum == target:
                max_length = max(max_length , j-i+1)
                
    return max_length
    
# def targetSumSubArrayBetter(nums , target):
    
#     hash_map = [0] * 20
#     for i in range(len(nums)):
#         hash_map[nums[i]]+=1

#     print(hash_map)
#     for i in range(len(hash_map)):
#         summ = 0
#         maxlength = 0
#         summ += hash_map[i]
#         if summ == target:
#             maxlength = i+1
    
#         remaining_sum = target - summ
#         if remaining_sum >= 0 and remaining_sum < len(hash_map):
#             length = i - hash_map[remaining_sum] 
#             maxlength = max(maxlength , length)    
#     return maxlength
             



if __name__ == "__main__":
    arr = [1,1,3,4,5,5,3]
    # print(targetSumSubArray(arr, 5))
    # # print(findNumApperanceOnce(arr))
    # print(targetSumSubArrayBetter(arr, 5))
    d = {}
    target = 5
    for i,j in enumerate(arr):
        if target - j in d:
            print(f"Pair found: ({j}, {target - j})")
            print(f"Pair found at index from {d[target-j]} to {i}")
        d[j] = i
    print(d)