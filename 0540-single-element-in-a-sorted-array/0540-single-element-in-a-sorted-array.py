class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        while(l<=h):
            mid = (l+h)//2
            if(n==1):
                return nums[mid]
            if(mid==0 and nums[0]!=nums[1]):
                return nums[mid]
            if(mid==n-1 and nums[n-1]!=nums[n-2]):
                return nums[mid]
            if(nums[mid-1]!=nums[mid]!=nums[mid+1]):
                return nums[mid]
            if(mid%2==0):
                if(nums[mid-1]==nums[mid]):
                    h = mid-1
                else:
                    l = mid+1
            else:
                if(nums[mid-1]==nums[mid]):
                    l = mid+1
                else:
                    h = mid-1
        return ans