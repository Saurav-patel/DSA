def targetSum(arr,target):
    mp = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in mp:
            return (mp[diff],i)
        mp[arr[i]] = i

if __name__ == "__main__":
    arr = [1,2,3,1,1,2]

    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0)+1

    # print(freq)
    print(targetSum(arr,4))

