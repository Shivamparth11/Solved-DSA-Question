import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        hi = max(piles)
        ans = hi
        while(l<=hi):
            mid = (l+hi)//2
            t = self.fun(piles,mid)
            if(t<=h):
                ans = mid
                hi = mid-1
            else:
                l = mid+1
        return ans
    def fun(self,piles,speed):
        n = len(piles)
        t = 0
        for i in range(n):
            t += math.ceil(piles[i]/speed)
        return t   