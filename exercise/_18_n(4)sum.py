from typing import List

def NSum(nums: List[int], N, target: int) -> List[List[int]]:
    nums.sort()
    res = []#结果
    tmp = []#前缀

    def sumhelper(nums, N, target, tmp, res):
        if len(nums) < N or nums[0]>target:
            return
        if N == 2:
            bg = 0
            ed = len(nums) - 1
            while bg < ed:
                if nums[bg] + nums[ed] > target:
                    ed -= 1
                elif nums[bg] + nums[ed] < target:
                    bg += 1
                else:
                    res.append(tmp + [nums[bg], nums[ed]])
                    bg += 1
                    while nums[bg] == nums[bg-1]:
                        bg += 1
                    ed -= 1
            return

        else:
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                sumhelper(nums[i + 1:], N - 1, target - nums[i], tmp+[nums[i]], res)

    sumhelper(nums, N, target, tmp, res)
    return res


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    print(NSum(nums,5,0))