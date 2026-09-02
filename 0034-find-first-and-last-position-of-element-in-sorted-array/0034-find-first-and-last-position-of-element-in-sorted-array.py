class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def fir(nums,target,ans,l,h):
            while(l<=h):
                mid = (l+h)//2
                if(nums[mid]==target):
                    ans = mid
                    h = mid-1
                elif(nums[mid]<target):
                    l = mid+1
                else:
                    h =mid-1
            return ans
        def las(nums,target,ans,l,h):
            while(l<=h):
                mid = (l+h)//2
                if(nums[mid]==target):
                    ans = mid
                    l=mid+1
                elif(nums[mid]<target):
                    l = mid+1
                else:
                    h =mid-1
            return ans
        return[fir(nums,target,-1,0,n-1),las(nums,target,-1,0,n-1)]