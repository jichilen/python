def max_profit(nums):
    p1 = 0
    p2 = 0
    lastmax = -1
    for i in range(len(nums)):
        if nums[i] < nums[p1]:
            p1 = i
        if nums[i] > nums[p2]:
            p2 = i
        if p2>p1:
            lastmax = max(nums[p2]-nums[p1],lastmax)
    return p1,p2,lastmax

if __name__ == '__main__':
    nums = [9, 11, 8, 5, 7, 12, 16, 14]
    print(max_profit(nums))
