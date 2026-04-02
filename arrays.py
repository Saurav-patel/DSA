
def secondLargest(nums):
    if len(nums) < 2:
        return -1
    largest = float("-inf")
    secondLargest = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            secondLargest = largest
            largest = nums[i]
        elif nums[i] > secondLargest and nums[i] != largest:
            secondLargest = nums[i]
    return secondLargest

def secondSmallest(nums):
    if len(nums) < 2:
        return -1
    smallest = float("inf")
    secondSmallest = float("inf")
    for i in range(len(nums)):
        if nums[i] < smallest:
            secondSmallest = smallest
            smallest = nums[i]
        elif nums[i] < secondSmallest and nums[i] != smallest:
            secondSmallest = nums[i]
    return secondSmallest

def checkSorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

def adjustleftByOne(nums):
    first = nums[0]
    for i in range(1,len(nums)):
        nums[i-1] = nums[i]
    nums[-1] = first
    return nums

def duplicate(nums):
    
    temp = []
    for i in range(len(nums)-1):
        for j in range(i+1 , len(nums)):
            if nums[i] == nums[j] and nums[i] not in temp:
                temp.append(nums[i])
    return temp

def removeDuplicate(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j] == nums[i]:
                nums.pop(j)
    return nums

def removeDuplicate2(nums):
    temp = []
    for i in range(len(nums)):
        if nums[i] not in temp:
            temp.append(nums[i])
    return temp

def shiftByK(nums , k):
    first = nums[k]
    for i in range(k,len(nums)):
        nums[i - k] = nums[i]
    nums[-k] = first
    return nums

if __name__ == "__main__":
    arr = [7,4,1,5,3]
    arr2 = [1,1,2,2,3,4,5]
    # print(secondLargest(arr))
    # print(secondSmallest(arr))
    # print(checkSorted(arr))
    # # print(checkSorted(arr2))
    # print(adjustleftByOne(arr))
    # print(duplicate(arr2))
    # # print(removeDuplicate(arr2))
    # print(removeDuplicate2(arr2))
    print(shiftByK(arr, 3))