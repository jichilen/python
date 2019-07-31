from typing import List
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        cal = 0
        for i in range(32):
            tmp = 0
            for i in range(len(nums)):
                if nums[i]&1==0:
                    tmp+=1
                nums[i] = nums[i]>>1
            cal = cal+(len(nums)-tmp)*tmp
        return cal

if __name__ == '__main__':
    so = Solution()
    print(so.totalHammingDistance([4,14,2]))