import random
import heapq

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


def quicksort(nums, bg, ed):
    '''
    找基准值，分左右两边，直接完成基准值的排序
    :param nums:
    :return:
    '''
    ind = quicksorthelper(nums, bg, ed)
    if ind < 0:
        return
    quicksort(nums, bg, ind)
    quicksort(nums, ind + 1, ed)


def quicksorthelper(nums, bg, ed):
    if ed - bg <= 1:
        return -1
    p = bg + 1
    psmall = bg
    while p < ed:
        if nums[p] <= nums[bg]:
            psmall += 1
            nums[p], nums[psmall] = nums[psmall], nums[p]
        p = p + 1
    nums[bg], nums[psmall] = nums[psmall], nums[bg]
    return psmall


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
    ln = len(nums)
    for i in range(ln // 2 - 1, -1, -1):
        heap_swap(nums, i, ln)
    for l in range(ln - 1, -1, -1):
        nums[l], nums[0] = nums[0], nums[l]
        heap_swap(nums, 0, l)


def heap_swap(nums, k, l):
    tmp = nums[k]
    while 2 * k + 1 < l:
        p = 2 * k + 1
        if p+1<l and nums[p]<nums[p+1]:
            p += 1
        if tmp < nums[p]:
            nums[k] = nums[p]
            k = p
        else:
            break
    nums[k] = tmp

def heapsort_offi(iterable):
     h = []
     for value in iterable:
         heapq.heappush(h, value)
     return [heapq.heappop(h) for i in range(len(h))]

if __name__ == '__main__':
    numb = list(range(1000))
    random.shuffle(numb)
    print(numb)
    nums = numb.copy()
    bubblesort(nums)
    print(nums)
    nums = numb.copy()
    selectionsort(nums)
    print(nums)
    nums = numb.copy()
    insertsort(nums)
    print(nums)
    nums = numb.copy()
    re = mergesort(nums)
    print(re)
    nums = numb.copy()
    quicksort(nums, 0, len(nums))
    print(nums)
    nums = numb.copy()
    heapsort(nums)
    print(nums)
    nums = numb.copy()
    print(heapsort_offi(nums))

