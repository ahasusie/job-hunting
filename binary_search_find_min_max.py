class Solution(object):
    def peakIndexInMountainArray(self, A):
        l, r = 0, len(A)-1
        while l<=r:
            mid = l+(r-l)//2
            if A[mid] > A[mid+1]:
                r = mid-1
            else:
                l = mid+1

        print A[l], A[r]        
        return A[l]

    def findPeakElement(self, nums):
        # l , mid , r = 0, 0, len(nums)-1
        # while l+1 < r:
        #     mid = l + (r-l)//2
        #     if nums[mid] < nums[mid + 1]:
        #         l = mid
        #     else:
        #         r = mid 
        # return max(nums[l], nums[r])
        
        l, mid, r = 0, 0, len(nums)-1
        while l<r:
           mid = l+(r-l)//2
           if nums[mid] > nums[mid+1]:
               r = mid
           else:
               l = mid+1
        print nums[l], nums[r]
        return nums[l]

    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l+1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid 
        print nums[l], nums[r]
        return min(nums[l], nums[r])


nums = [3,4,5,1,2]
obj = Solution()
#obj.findMin(nums)
obj.findPeakElement(nums)
#obj.peakIndexInMountainArray(nums)
