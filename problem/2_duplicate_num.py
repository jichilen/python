'''
n个数范围0-n-1，找重复数字
两个常见思路
'''

def dump_num(nums):
    tmp = set()
    out = []
    for n in nums:
        if n not in tmp:
            tmp.add(n)
        else:
            out.append(n)
    return out

def dump_num2(nums):
    pass

if __name__ == '__main__':
    nums = [1,2,2,3,4,5,1]
    re = dump_num(nums)
    print(re)