class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        while(l<=h):
            mid = (l+h)//2
            if(n==1):
                return mid
            if(mid==0 and nums[mid]>nums[mid+1]):
                return mid
            if(mid==n-1 and nums[mid]>nums[mid-1]):
                return mid
            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid]>nums[mid-1]):
                l = mid+1
            else:
                h = mid-1
        return 1