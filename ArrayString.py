# arrays:
# - sliding window
# - rotation
# - order statistics
# - range query
# - search and sorting
# - optimization
# - matrix
# - arrangement and rearrangement
# - array transformation

# find pivot index
# searching: two halves
def pivotIndex(nums):
    if not nums:
        return -1
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

# largest number at least twice of others
# need to iterate every item in array
# searching: 
def dominantIndex(nums):
    if not nums: return -1
    m = max(nums)
    if all(m >= x**2 for x in nums if x != m):
        return nums.index(m)
    return -1

# plus one
def plusOne(nums):
    if not nums: return -1
    value = 0
    for i in range(len(nums)):
        value = value + nums[i] * (10**(len(nums)-i-1))
    value += 1
    return [int(i) for i in str(value)]

def moveZeroes(nums):
    count = nums.count(0)
    nums[:] = [i for i in nums if i != 0]
    nums += count*[0]

def twoSumII(nums, target):
    # for i in range(len(nums)):
    #     if target - nums[i] in nums:
    #         return [i, nums.index(target-nums[i])]

    l, r = 0, len(nums)-1
    while l<r:
        if nums[l] + nums[r] == target:
            return [l, r]
        elif nums[l] + nums[r] < target:
            l += 1
        else: 
            r -= 1
    return []

def removeDuplicate(nums):
    if not nums: return 
    slow = 0
    fast = 1
    while fast < len(nums)-1:
        print nums[slow], nums[fast]
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

def strStr(words, needle):
    # for i in range(len(words)-len(needle)+1):
    #     if words[i:i+len(needle)] == needle:
    #         return i
    # return -1
    l, r = 0, len(needle)
    while r <= len(words):
        if words[l:r] == needle:
            return l
        else:
            l += 1
            r += 1
    return -1

def threeSums(nums):
    res = []
    nums.sort()
    if len(nums) < 3:
        return res
    
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l<r:
            s = nums[i]+nums[l]+nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res

#nums = [1,1,2,3,3,5]
#print strStr("hello", "ll")
#print removeDuplicate(nums)
#print twoSumII(nums, 9)
# matrix rotation
# - spinral rotation
# - clockwise/anti-clockwise
# - transpose

# transpose
def transposeMatrix(A):
    R, C = len(A), len(A[0])
    ans = [[None] * R for _ in xrange(C)]
    for i, row in enumerate(A):
        for j, val in enumerate(row):
            ans[j][i] = val
    return ans

# strings:
# - arthimatic operation in string
# - character counting 
# - subsequence and substring
# - reverse and rotation
# - sorting and searching
# - case sensitive string
# - occurrence problem
# - pattern searching
# - split string

# == if need to change char value of a string, must change string into array

def testString(words):
    char = list(words)
    char[3] = 'k'
    return char

def reverseStr(words):
    arr = list(words)
    l, r = 0, len(arr)-1
    while l<r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return ''.join(arr)

def validPal(words):
    words = words.strip()
    l, r = 0, len(words)-1
    while l<r:
        if not words[l].isalnum():
            l += 1
        elif not words[r].isalnum():
            r -= 1
        else:
            if words[l].lower() != words[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True

def reverseVowel(words):
    vowels = set(list("aeiouAEIOU"))
    words = list(words)
    l, r = 0, len(words)-1
    while l<r:
        if words[l] not in vowels:
            l += 1
        elif words[r] not in vowels:
            r -= 1
        else:        
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
    return ''.join(words)

def backspaceStrComp(s, t):
    def stackCheck(words, stack):
        for c in words:
            if c is not '#':
                stack.append(c)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack
    s1 = stackCheck(s, [])
    s2 = stackCheck(t, [])
    return s1 == s2
  
def lengthOfLongestSubstring(s):
    dic, cnt, l = {}, 0, 0       

    for r in range(len(s)):
        if s[r] in dic and l <= dic[s[r]]:
            l = dic[s[r]] + 1
            
        else:
            cnt = max(cnt, r - l + 1)
        dic[s[r]] = rq
    return cnt

def repeatedSubstringPattern(str):
    if not str: return False
    ss = (str+str)[1:-1]
    print ss
    return ss.find(str) != -1

print repeatedSubstringPattern("abcabc")
#print lengthOfLongestSubstring("abcabcbb")
#print backspaceStrComp("ab##", "c#d#")
#print reverseVowel("hello")
#print validPal("A man, a plan, a canal: Panama")
#print reverseStr("abcde")
#words = "shanshan"
#print testString(words)

# matrix = [
#             [1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9],
# ]
#print transposeMatrix(matrix)
#print plusOne(nums)
#print dominantIndex(nums)
#print pivotIndex(nums)