class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numdic = {}
from typing import List
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        maxl = 0
        for n in nums:
            if n-1 not in dic:
                curn = n
                tmpl = 1
                while curn+1 in dic:
                    curn,tmpl = curn+1,tmpl+1
                maxl = max(maxl,tmpl)
        return maxl




if __name__ == '__main__':
    so =Solution()
    nums = [100,4,200,1,2,3]
    print(so.longestConsecutive(nums))