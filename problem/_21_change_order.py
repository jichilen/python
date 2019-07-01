def change_order(nums, fun):
    if len(nums) == 0:
        return
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        if fun(nums[p1]):
            p1 += 1
        elif fun(nums[p2]):
            nums[p1], nums[p2] = nums[p2], nums[p1]
        else:
            p2 -= 1


def odd_first(num1):
    if num1 & 1 == 1:
        return True
    return False


def pos_first(num1):
    if num1 > 0:
        return True
    return False


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, -7, 8]
    change_order(nums, pos_first)
    print(nums)
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    change_order(nums, odd_first)
    print(nums)