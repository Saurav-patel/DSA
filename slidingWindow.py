
def maxSubArraywithK(nums,target):
    low = 0
    high = low+1
    temp = []
    summ = 0
    count = 0
    for high in range(len(nums)):
        summ += nums[high]

        
        while summ > target and low < high:
            summ -= nums[low]
            low += 1
        
        if summ == target:
            count = high - low + 1
            # temp.append(nums[low:high+1])

    return count 

def kadane(nums ):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1,len(nums)):
        current_sum = max(nums[i],current_sum + nums[i])
        

        max_sum = max(max_sum,current_sum)
         
    return max_sum 


if __name__ == "__main__":
    arr = [2,3,-4,5,-6,8]
    print(f"maximum subarray length with sum k = {maxSubArraywithK(arr , 12)}")
    print(f"maximum subarray sum = {kadane(arr )}")