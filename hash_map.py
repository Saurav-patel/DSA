def contains_duplicate(arr):
    mp = {}
    for num in arr:
        if num in mp:
            return True
        mp[num] = 1
    return False


def frequency_count(arr):
    mp = {}
    for num in arr:
        mp[num] = mp.get(num, 0) + 1
    return mp


def first_repeating_element(arr):
    mp = {}
    for num in arr:
        if num in mp:
            return num
        mp[num] = 1
    return -1


def first_non_repeating_char(s):
    mp = {}
    for ch in s:
        mp[ch] = mp.get(ch, 0) + 1
    for ch in s:
        if mp[ch] == 1:
            return ch
    return None

def non_repeating_characters(s):
    mp = {}
    for ch in s:
        mp[ch] = mp.get(ch, 0) + 1
    for ch in s:
        if mp[ch] == 1:
            print(f"{ch} is a non-repeating character")
    return -1

def sum_with_k(arr , k):
    mp = {}
    for nums in arr:
        diff = k - nums
        if diff in mp:
            return (diff, nums)
        mp[nums] = 1
    return None

def ransome_note(magzine , note):
    mp = {}
    for ch in (note):
        
        mp[ch] = mp.get(ch, 0) + 1
        print(mp)
    for ch in magzine:
        if ch in mp:
            print("word found", ch)
            mp[ch] -=1
            
            
    
        
        
    return all(value <= 0 for value in mp.values())

def maxWordFormation(words,target):
    mp_target = {}
    mp_words = {}
    for ch in target:
        mp_target[ch] = mp_target.get(ch, 0) + 1
    for ch in words:
        mp_words[ch] = mp_words.get(ch, 0) + 1
    count = float('inf')
    for ch in mp_target:
        if ch in mp_words:
            
            count = min(count  ,  mp_words[ch]// mp_target[ch])
        else:
            return 0
            
    return count

def longestPalindrome(str):
    length = 0
    mp = {}
    for ch in str:
        mp[ch] = mp.get(ch,0)+1
    
    for ch in mp:
        if mp[ch] % 2 == 0 :
            length+=mp[ch]
            
        else:
                length+=mp[ch]-1
                is_odd = True
            
        
    return length+1 if is_odd else length


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 1]
    # print(contains_duplicate(arr))
    # print(frequency_count(arr))
    # print(first_repeating_element(arr))
    # s = "hello world"
    # print(first_non_repeating_char(s))
    # print(non_repeating_characters(s))
    print(sum_with_k(arr, 6))
    print(ransome_note("abc", "a"))
    print(maxWordFormation("hhellod world", "hold"))
    print(longestPalindrome("aabbbbccddd"))