

def selectionSort(nums):
    for i in range(len(nums)-1):
        minn = i
        for j in range(i , len(nums)):
            if nums[j] < nums[minn]:
                minn = j
        arr[minn] , arr[i] = arr[i] , arr[minn]

    print(nums)


def bubbleSort(nums):
    for i in range(len(nums)-1 , 0 , -1):
        didSwap = 0
        
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1]  = nums[j+1] , nums[j]
                didSwap = 1
        if didSwap == 0:
            print("Array is in already sorted")
            break
    print(f"bubble sort: {nums}")
                
    


def insertionSort(nums):
    for i in range(1 ,len(nums)):
        
        
        for j in range(i, 0 , -1):
            
            if j >= 0 and nums[j] < nums[j-1]:
                nums[j] , nums[j-1] = nums[j-1] , nums[j]
            else:
                break
    print(f"Insertion Sort : {nums}") 
class Solution:
    def merge(self ,nums ,low , mid , high):
        temp = []
        left , right = low , mid+1
        while left <= mid and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        
        while left<= mid:
            print(f"left: {left} , mid: {mid}")
            temp.append(nums[left])
            left+=1
        while right<= high:
            print(f"right: {right} , high: {high}")
            temp.append(nums[right])
            right+=1

        for i in range(low, high+1):
            nums[i]  = temp[i-low]
        
    def mergeSort(self, nums, low , high):
        if low>=high:
            return
        mid = (low+high)//2
        self.mergeSort(nums,low,mid)
        self.mergeSort(nums,mid+1,high)
        return self.merge(nums,low,mid,high)
        
    
def recursiveBubbleSort(nums , n):
    if n == 1:
        return
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i] , nums[i+1] = nums[i+1] , nums[i]
    recursiveBubbleSort(nums , n-1)
    
def recursiveSelectionSort(nums , index):
    if index == (len(nums)-1):
        return
    minn = index
    for i in range(minn , len(nums)):
        if nums[i] < nums[minn]:
            minn = i
    nums[index] , nums[minn] = nums[minn] , nums[index]
    recursiveSelectionSort(nums , index+1)

if __name__ == "__main__":
    arr = [7,4,1,5,3]
    arr2 = [1,2,3,4,5]
    # high = len(arr)-1
    # sn = Solution()
    # sn.mergeSort(arr , 0 , high)
    # print(arr)
    # recursiveBubbleSort(arr , len(arr))
    recursiveSelectionSort(arr , 0)
    print(arr)



    # selectionSort(arr)
    # bubbleSort(arr)
    # bubbleSort(arr2)
    #insertionSort(arr)
    
    