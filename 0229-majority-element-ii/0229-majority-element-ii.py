class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1,cnt2 =0,0
        el1 = None
        el2 = None
        for i in range(n):
            if(cnt1==0 and el2 != nums[i]):
                cnt1 = 1
                el1 = nums[i]
            elif(cnt2 == 0 and el1 != nums[i]):
                cnt2 = 1
                el2 = nums[i]
            elif(el1==nums[i]):
                cnt1+=1
            elif(el2 == nums[i]):
                cnt2+=1
            else: 
                cnt1-=1
                cnt2-=1
        cnt1,cnt2 = 0,0
        for i in range(n):
            if(el1==nums[i]):
                cnt1+=1
            if(el2==nums[i]):
                cnt2+=1
        ls = []
        max = n//3
        if(cnt1>max):
            ls.append(el1)
        if(cnt2>max):
            ls.append(el2)
        return ls