from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxj = 0
        for i in range(len(nums)):
            if i>maxj:
                return False
            maxj = max(maxj,i+nums[i])
        return True



if __name__ == '__main__':
    so = Solution()
    print(so.canJump([2,3,1,1,4]))