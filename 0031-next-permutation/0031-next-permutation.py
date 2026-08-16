class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        p = -1
        for i in range(n-2,-1,-1):
            if(nums[i]<nums[i+1]):
                p = i
                break
        if(p == -1):
            nums.reverse()
            return
        for i in range(n-1,p,-1):
            if(nums[i]>nums[p]):
                nums[i],nums[p]=nums[p],nums[i]
                break
        i=p+1
        j=n-1
        while(i<=j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1