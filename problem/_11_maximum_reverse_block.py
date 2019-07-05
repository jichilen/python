
'''
这是一个分治问题
直接的来看需要二分，二分之后会有几种情况

1.中间元素大于在三数中最大 [3,4,5,1,2] [3,4,5,6,7,1,2]
2.中间元素在三数中最小 [4,5,1,2,3] [6,7,1,2,3,4,5]
无论怎么分有一边一定是顺序的，这边没有最小值
如何判断顺序？  第一个值小于最后一个值
'''

def reverse_list(nums,bg,ed):
    #TODO: 这个例子有一个特例
    # 说是递增，没有强调严格递增
    # [1,0,1,1,1,1] 和 [1,1,1,1,0,1]总会出错一个
    if len(nums)==0:
        return None

    while bg < ed:
        mid = (bg + ed) // 2
        if nums[mid]>nums[ed]:
            bg = mid +1
        elif nums[mid] == nums[ed]:
            ed -= 1
        else:
            ed = mid
    return nums[bg]


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    nums = [3,4,5,1,2]
    nums = [1,1,1,1,0,1]
    nums = [6,7,1,2,3,4,5]
    nu = reverse_list(nums,0,len(nums)-1)
    print(nu)