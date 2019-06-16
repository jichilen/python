def bubblesort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


def selectionsort(nums):
    for i in range(len(nums)):
        minid = i
        for j in range(i, len(nums)):
            if nums[minid] > nums[j]:
                minid = j
        nums[i], nums[minid] = nums[minid], nums[i]


def insertsort(nums):
    for i in range(len(nums)):
        for j in range(i):
            j = i - j - 1
            t = j + 1
            if nums[j] > nums[t]:
                nums[t], nums[j] = nums[j], nums[t]
            else:
                break


def shellsort(nums):
    pass


def quicksort(nums):
    '''
    找基准值，分左右两边，直接完成基准值的排序
    :param nums:
    :return:
    '''
    pass


def mergesort(nums):
    '''
    归并排序由于需要对排序后的子序列重拍，所以需要额外的空间
    :param nums:
    :return:
    '''
    l = len(nums)
    if l <= 1:
        return nums
    mid = (0 + l) // 2
    left = nums[:mid]
    right = nums[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


def merge(left, right):
    out = []
    p1 = p2 = 0
    while p1 < len(left) or p2 < len(right):
        if p1 >= len(left):
            out.extend(right[p2:])
            break
        if p2 >= len(right):
            out.extend(left[p1:])
            break
        if left[p1] < right[p2]:
            out.append(left[p1])
            p1 += 1
        else:
            out.append(right[p2])
            p2 += 1
    return out


def heapsort(nums):
    '''
    构建堆，交换构建堆
    :param nums:
    :return:
    '''
    pass


if __name__ == '__main__':
    nums = [1, 12, 1, 6, 7, 8, 3, 5, 11]
    insertsort(nums)
    print(nums)
    nums = [1, 1, 3, 5, 6, 7, 8, 11, 12]
    re = mergesort(nums)
    print(re)
