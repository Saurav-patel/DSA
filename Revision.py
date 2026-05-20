def targetSum(arr,target):
    mp = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in mp:
            return (mp[diff],i)
        mp[arr[i]] = i



def substringLongestWithoutRepeating(s):
    mp = {}
    start  = 0
    max_length = 0
    for end in range(len(s)):
        if s[end] in mp and mp[s[end]] >= start:
            start = mp[s[end]] + 1
            print("start =", start)
        mp[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length

def numAppearMoreThanOnce(arr):
    mp = {}
    res = []
    for i in range(len(arr)):
        if arr[i] in mp and mp[arr[i]] >= 1:
            # res.append(arr[i])
            return arr[i]
        mp[arr[i]] = mp.get(arr[i],0)+1
    # return -1
    return res

if __name__ == "__main__":
    arr = [1,2,3,1,1,2]

    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0)+1

    # print(freq)
    print(targetSum(arr,4))
    print(substringLongestWithoutRepeating("abcabcbb"))
    print(substringLongestWithoutRepeating("bcdefg"))
    print(numAppearMoreThanOnce(arr))
