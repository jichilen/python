def maxsum_of_subvec(nums):
    pastmax = -1
    out = -1
    for i in range(len(nums)):
        out = maxsum(nums,i,out)
        if out>pastmax:
            pastmax = out
    return pastmax


def maxsum(nums,i,lastmax):
    nowmax = nums[i]+lastmax
    return max(nowmax,nums[i])



if __name__ == '__main__':
    nums = [1,-2,3,10,-4,7,2,-5]
    print(maxsum_of_subvec(nums))