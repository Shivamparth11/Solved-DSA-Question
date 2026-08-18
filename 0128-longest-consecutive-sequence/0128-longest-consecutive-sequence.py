class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        new_set=set(nums)
        longest = 0
        for num in new_set:
            if num-1 not in new_set:
                cnt = 1
                x = num
                while x+1 in new_set:
                    x+=1
                    cnt+=1
                longest = max(longest,cnt)
        return longest