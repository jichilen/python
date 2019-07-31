from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        def swp(nums,a,b):
            nums[a]^=nums[b]
            nums[b]^=nums[a]
            nums[a]^=nums[b]

        for i in range(len(nums)):
            while nums[i]!=i+1:
                if nums[i] != nums[nums[i]-1]:
                    swp(nums,i,nums[i]-1)
                else:
                    break
        out = []
        for i in range(len(nums)):
            if nums[i]!=i+1:
                out.append(i+1)
        return out


if __name__ == '__main__':
    so = Solution()
    print(so.findDisappearedNumbers([4,3,2,7,8,2,3,1]))