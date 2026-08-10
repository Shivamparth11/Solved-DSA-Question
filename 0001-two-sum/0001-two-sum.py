class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i,num in enumerate(nums):
            res = target - num
            if res in sum:
                return [sum[res],i]
            sum[num] = i
        return []
