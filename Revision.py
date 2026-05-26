def targetSum(arr,target):
    mp = {}
    for i in range(len(arr)):
        diff = target - arr[i]
        if diff in mp:
            return (mp[diff],i)
        mp[arr[i]] = i


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

def minSubArrayWithSumK(arr , target):
    low = 0
    
    summ = 0
    min_length = float("inf")
    for high in range(len(arr)):
        summ += arr[high]
        while summ >= target:
            min_length = min(min_length, high - low + 1)
            summ -= arr[low]
            low += 1
    return min_length if min_length != float("inf") else 0


def maxSubArraywithSumSmallerorEqualK(arr , target):
    low = 0
    summ = 0
    max_len = 0
    high = 0
    for high in  range(len(arr)):
        summ += arr[high]
        while summ > target:
            max_len = max(max_len,high-low)
            summ -= arr[low]
            low+=1
    return max_len,arr[low:high+1]

def minSubArrayWithSumGreaterorEqualK(arr,target):
    low = 0
    summ = 0
    high = 0
    min_len = float("inf")
    for high in range(len(arr)):
        summ += arr[high]
        while summ >= target:
            min_len = min(min_len, high - low + 1)
            summ -= arr[low]
            
            low += 1
    
    return min_len,arr[low-1:high+1] if min_len != float("inf") else 0
    
def longestPalindrome(str):
    low =0
    high = len(str)-1
    length = 0
    while low < high:
        if str[low] == str[high]:
            length += 2
            low+=1
            high-=1
        else:
            high-=1
    if low == high:
        length+=1
    return length,str[low:high+1]


def minWindowSubstring(s,t):
    def check(have,required):
        for i in range(128):
            if have[i] < required[i]:
                return False
        return True
    low = 0
    start = 0
    res = float("inf")
    required = [0]*128
    have = [0]*128
    for ch in t:
        required[ord(ch)] += 1
    for high in range(len(s)):
        have[ord(s[high])] +=1
        while check(have,required):
            curr_len = high-low+1
            if curr_len < res:
                res = curr_len
                start = low
            have[ord(s[low])] -= 1
            low += 1
    return s[start:start+res] if res != float("inf") else ""
        

if __name__ == "__main__":
    arr = [1,2,3,1,1,2]

    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0)+1

    # # print(freq)
    # print(targetSum(arr,4))
    # print(substringLongestWithoutRepeating("abcabcbb"))
    # print(substringLongestWithoutRepeating("bcdefg"))
    # print(numAppearMoreThanOnce(arr))
    # print(minSubArrayWithSumK(arr, 7))
    print(maxSubArraywithSumSmallerorEqualK(arr, 7))
    print(minSubArrayWithSumGreaterorEqualK(arr, 7))
    print(longestPalindrome("babad"))
    print(minWindowSubstring("ADOBECODEBANC","ABC"))