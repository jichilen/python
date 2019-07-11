import random
def partition(nums, bg, ed):
    fl = bg
    for i in range(bg + 1, ed):
        if nums[i] < nums[bg]:
            fl += 1
            nums[i], nums[fl] = nums[fl], nums[i]
    nums[bg], nums[fl] = nums[fl], nums[bg]
    return fl


def min_k(nums, k):
    bg = 0
    ed = len(nums)
    if ed < k:
        return
    if ed == k:
        return nums
    ind = partition(nums, bg, ed)
    while ind != k:
        if ind > k:
            ed = ind
        else:
            bg = ind+1
        ind = partition(nums, bg, ed)
    return nums[:ind]

if __name__ == '__main__':
    k = 4
    nums = list(range(10))
    random.shuffle(nums)
    print(min(nums,k))