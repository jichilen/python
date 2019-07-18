def poker_in_order(nums):
    nums.sort()
    c_0 = 0
    gap = 0
    for i in range(1,len(nums)):
        if nums[i-1]==0:
            c_0+=1
            continue
        gap = gap+nums[i]-nums[i-1]-1
    if gap<=c_0:
        return True
    return False



if __name__ == '__main__':
    print(poker_in_order([1,2,3,4,6]))
    print(poker_in_order([1,1,3,4,6]))
    print(poker_in_order([2,1,3,4,6]))
    print(poker_in_order([0,2,3,4,6]))
    print(poker_in_order([0,0,3,6,7]))
    print(poker_in_order([0, 0, 3, 6, 8]))
