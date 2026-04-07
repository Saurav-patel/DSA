
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

def zeroesToEnd(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < len(nums):
        nums[count] = 0
        count += 1
    return nums
def fun(nums):
    high =  len(nums) - 1
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i], nums[high] = nums[high], nums[i]
            high -= 1
    return nums


def targetSum(nums , target):
    sum = 0
    temp = []
    for i in range(len(nums)):
        for j in range(len(nums)-1,i , -1):
            sum = nums[i] + nums[j]
            if sum == target:
                temp.append((nums[i], nums[j]))
    return temp

def union(nums1 , nums2):
    for i in range(len(nums1)):
        for j in range(len(nums1)-1,i,-1):
            if nums1[i] > nums1[j]:
                nums1[i], nums1[j] = nums1[j], nums1[i]
    for i in range(len(nums2)):
        for j in range(len(nums2)-1,i,-1):
            if nums2[i] > nums2[j]:
                nums2[i], nums2[j] = nums2[j], nums2[i]

    for i in range(len(nums2)):
        if nums2[i] not in nums1:
            nums1.append(nums2[i])
    return nums1

def optimalUnionOfSortedArrays(nums1 , nums2):
    temp = []
    i , j = 0 , 0
    while i<len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if not temp or temp[-1] != nums1[i]:

                temp.append(nums1[i])
            i+=1
        elif nums2[j] < nums1[i]:
            if not temp or temp[-1] != nums2[j]:
                temp.append(nums2[j])
            j+=1
        
        else:
            if not temp or temp[-1] != nums1[i]:
                temp.append(nums1[i])
            i+=1
            j+=1

    while i < len(nums1) :
        if not temp or temp[-1] != nums1[i]:
            temp.append(nums1[i])
        i+=1
    while j < len(nums2) :
        if not temp or temp[-1] != nums2[j]:
            temp.append(nums2[j])
        j+=1
    
    return temp

def union2(nums1,nums2):
    temp = set(nums1)
    for i in range(len(nums2)):
        temp.add(nums2[i])
    return list(temp)

def intersection(nums1 , nums2):
    result = []
    i , j = 0 ,  0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
    return result


def findMissing(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    print(f"Total sum of first {n} natural numbers: {total_sum}")
    arr_sum = 0
    for i in range(len(nums)):
        arr_sum += nums[i]
    return total_sum - arr_sum

def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

def findNumApperanceOnce(nums):
    # optimal solution using XOR operator
    # xor_result = 0
    # for i in range(len(nums)):
    #     xor_result ^= nums[i]
    # return xor_result

    # better solution using hash map
    # hash_map = [0] * 10
    # for i in range(len(nums)):
    #     hash_map[nums[i]]+=1
    # for i in range(len(hash_map)):
    #     if hash_map[i] == 1:
    #         return i
        
    # brute force solution
    # for i in range(len(nums)):
    #     num = nums[i]
    #     count = 0
    #     for j in range(len(nums)):
    #         if nums[j] == num:
    #             count +=1
    #     if count == 1:
    #         return num
    # return -1


if __name__ == "__main__":
    arr = [7,4,1,1,10,0,5,3,3,3]
    arr2 = [1,1,2,2,3,3,4,5,5]
    arr3 = [1,2,4,5]
    # print(secondLargest(arr))
    # print(secondSmallest(arr))
    # print(checkSorted(arr))
    # # print(checkSorted(arr2))
    # print(adjustleftByOne(arr))
    # print(duplicate(arr2))
    # # print(removeDuplicate(arr2))
    # print(removeDuplicate2(arr2))
    # print(shiftByK(arr, 3))
    # print(zeroesToEnd(arr))

    # print(fun(arr))
    # print(f"sum of two numbers equal to 7: {targetSum(arr, 7)}")
    # print(f"Union of arr and arr2: {union(arr, arr2)}")
    # print(f"Optimal Union of arr and arr2: {optimalUnionOfSortedArrays(arr, arr2)}")
    # # print(f"Union of arr and arr2 (using set): {union2(arr, arr2)}")
    # print(f"Intersection of arr and arr2: {intersection(arr, arr2)}")
    # # print(f"Missing number in arr: {findMissing(arr3)}")
    # print(f"Maximum consecutive ones in arr: {findMaxConsecutiveOnes(arr)}")
    print(f"Number that appears only once in arr: {findNumApperanceOnce(arr2)}")