
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
            temp.append(nums[low:high+1])

    return count , temp 


def minSubArraywithK(nums,target):
    low = 0
    high = low + 1
    summ = 0
    start , end = 0 , 0
    min_length = float("inf")
    for high in range(len(nums)):
        summ += nums[high]
        while summ >= target :
            if high - low + 1 < min_length:
                min_length = high - low + 1
                start , end = low , high
            summ -= nums[low]
            low += 1

        

    return min_length , nums[start:end+1]

def allPossibleSubArrays(nums , target):
    subArray = []
    low , high = 0 , 0
    summ = 0
    for high in range(len(nums)):
        summ+= nums[high]
        while summ >= target and low < high:
            subArray.append(nums[low:high+1])
            summ -= nums[low]
            low += 1
    return subArray

def kadane(nums ):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1,len(nums)):
        current_sum = max(nums[i],current_sum + nums[i])
        

        max_sum = max(max_sum,current_sum)
         
    return max_sum 

def staticWindow(nums , k ):
    windowSum = sum(nums[:k])
    maxSumm = windowSum
    temp = [nums[:k]]
    for i in range(k,len(nums)):
        windowSum += nums[i]
        windowSum -= nums[i-k]
        if windowSum > maxSumm:
            maxSumm = windowSum
            temp = (nums[i-k+1:i+1]) 
    return maxSumm , temp


def staticWindow2(nums , k):
    summ = 0
    low = 0
    high = low + k - 1
    maxSumm = 0
    for i in range(low,high+1):
        summ += nums[i]
        maxSumm = summ
    while high < len(nums)-1:
        high +=1
        summ += nums[high]
        summ -= nums[low]
        low += 1
        maxSumm = max(maxSumm , summ)
    return maxSumm, nums[low:high+1]
    

if __name__ == "__main__":
    arr = [2,3,4,5,6,8]
    print(f"maximum subarray length with sum k = {maxSubArraywithK(arr , 23)}")
    print(f"minimum subarray length with sum k = {minSubArraywithK(arr , 22)}")
    print(f"all possible subarrays with sum greater than or equal to k = {allPossibleSubArrays(arr , 23)}")
    print(f"maximum subarray sum = {kadane(arr )}")
    print(f"static window = {staticWindow(arr , 3)}")
    print(f"static window 2 = {staticWindow2(arr , 3)}")
