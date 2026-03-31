

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


if __name__ == "__main__":
    arr = [7,4,1,5,3]
    arr2 = [1,2,3,4,5]
    
    
    
    # selectionSort(arr)
    # bubbleSort(arr)
    # bubbleSort(arr2)
    insertionSort(arr)
