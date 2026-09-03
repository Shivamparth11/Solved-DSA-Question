class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        h = n-1
        ans = max(nums)
        while(l<=h):
            mid = (l+h)//2
            if(nums[l]<=nums[mid]):
                ans = min(ans,nums[l])
                l = mid+1
            else:
                ans = min(ans,nums[mid])
                h = mid-1
        return ans