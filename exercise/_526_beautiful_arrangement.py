class Solution:
    def countArrangement(self, N: int) -> int:
        tmp = list(range(N+1))
        count = [0]
        def helper(nums,sid):
            if sid == len(nums):
                count[0] = count[0] + 1
            for i in range(sid,len(nums)):
                if nums[i]%sid==0 or sid%nums[i]==0:
                    nums[sid],nums[i] = nums[i],nums[sid]
                    helper(nums,sid+1)
                    nums[sid], nums[i] = nums[i], nums[sid]
        helper(tmp,1)
        return count


if __name__ == '__main__':
    so = Solution()
    print(so.countArrangement(5))