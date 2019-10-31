from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()
        out = []
        for i,x in enumerate(nums):
            if x in dic:
                out.append([dic[x],i])
            else:
                dic[target-x]=i
        return out[0]