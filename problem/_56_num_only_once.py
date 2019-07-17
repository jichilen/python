def num_only_once(nums):
    if len(nums)==0:return None
    out = nums[0]
    for i in nums[1:]:
        out = out ^ i
    sp1 = []
    sp2 = []
    tmp = out&(out-1)
    out = out^tmp
    for i in nums:
        if out & i == out:
            sp1.append(i)
        else:
            sp2.append(i)
    return sp1,sp2


if __name__ == '__main__':
    num_only_once([1,2,4,6,3,2,5,5,4,1])