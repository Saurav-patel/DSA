

def selectionSort(nums):
    for i in range(len(nums)-1):
        minn = i
        for j in range(i , len(nums)):
            if nums[j] < nums[minn]:
                minn = j
        arr[minn] , arr[i] = arr[i] , arr[minn]

    print(nums)



if __name__ == "__main__":
    arr = [7,4,1,5,3]
    
    
    
    selectionSort(arr)