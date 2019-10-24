def all_list_of_str(str1):
    def helper(str1):
        if len(str1) == 0:
            return [[]]
        result = []
        for i in range(len(str1)):
            out = helper(str1[:i]+str1[i+1:])
            for x in out:
                x.append(str1[i])
                result.append(x)
        return result
    return helper(str1)

def all_sort(nums):
    out = []
    def helper(nums,bg):
        if bg == len(nums)-1:
            out.append(nums.copy())
            return
        for i in range(bg,len(nums)):
            nums[i],nums[bg] = nums[bg],nums[i]
            helper(nums,bg+1)
            nums[i], nums[bg] = nums[bg], nums[i]
    helper(nums,0)
    return out


if __name__ == '__main__':
    str1 = ['a','b','c','d']
    print(all_sort(str1))