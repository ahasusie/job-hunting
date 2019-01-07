def pivotIndex(nums):
    if not nums: return -1
    for i, n in enumerate(nums):
        if sum(nums[:i]) == sum(nums[i+1:]):
            return i
    return -1

def largestNumber(nums):
    if not nums: return -1
    m = max(nums)
    if all(m >= 2*n for n in nums if n != m):
        return nums.index(m)

def plusOne(nums):
    if not nums: return -1
    value = 0
    for i in range(len(nums)):
        value = value + nums[i]*10**(len(nums)-1-i)
    return [int(c) for c in str(value+1)]

def transMatrix(nums):
    r, c = len(nums), len(nums[0])
    ans = [[None]*r for _ in range(c)]
    for i, row in enumerate(nums):
        for j, val in enumerate(row):
            ans[j][i] = val
    return ans

def rmElement(nums, val):
    if not nums: return -1
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = val 
            i += 1
    return i

def reverseStr(string):
    if not string: return None
    i, j = 0, len(string)-1
    l = list(string)
    while i<j:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return ''.join(l)

def moveZero(nums):
    # if not nums: return None
    # for i in range(len(nums)):
    #     if nums[i] == 0 and i+1 <= len(nums)-1:
    #         nums[i], nums[i+1] = nums[i+1], nums[i]
    #     else:
    #         continue
    # return nums
    slow, fast = 0, 0
    while fast <= len(nums)-1:
        if nums[fast] is not 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
        print slow, fast
    return nums

def twoSum(nums, sums):
    l, r = 0, len(nums)-1
    while l<r:
        s = nums[l]+nums[r]
        if s == sums:
            return [l+1, r+1]
        elif s < sums:
            l += 1
        else:
            r -= 1
    return None

def validPalindrome(s):
    l, r = 0, len(s)-1
    while l<r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
    return True

def reverseVowels(word):
    vowels = set(list("aeiouAEIOU"))
    s = list(word)
    l, r = 0, len(s)-1
    while l<r:
        if s[l] not in vowels:
            l += 1
        elif s[r] not in vowels:
            r -= 1
        else:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    return ''.join(s)

def backspaceCompare(S, T):
    def stack(string, stack):
        for char in string:
            if char != '#':
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()
        return stack

    l1 = stack(S, [])
    l2 = stack(T, [])
    return l1 == l2


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = "race a car"

    print backspaceCompare("ab#c", "ad#c")
    # print reverseVowels("hello")
    # print validPalindrome(s)
    # print twoSum(nums, 4)
    # print moveZero(nums)
    # print reverseStr(s)
    # print rmElement(nums, 9)
    # print transMatrix(matrix)
    # print plusOne(nums)
    # print largestNumber(nums)
    # print pivotIndex(nums)
