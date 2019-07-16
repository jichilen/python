def times_in_sort(nums, target):
    if len(nums) == 1: return 0
    def find_first(nums,target,bg,ed):
        if bg>ed:
            return -1
        mid = (ed+bg)//2
        if nums[mid]==target:
            if mid>0 and nums[mid-1]<target or mid==0:
                return mid
            else:
                return find_first(nums,target,bg,mid-1)
        elif nums[mid]>target:
            return find_first(nums,target,bg,mid-1)
        else:
            return find_first(nums,target,mid+1,ed)

    def find_last(nums, target, bg, ed):
        if bg > ed:
            return -1
        mid = (ed + bg) // 2
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid + 1] > target or mid == len(nums)-1:
                return mid
            else:
                return find_last(nums, target, mid + 1, ed)
        elif nums[mid] > target:
            return find_last(nums, target, bg, mid - 1)
        else:
            return find_last(nums, target, mid + 1, ed)
    l = find_first(nums,target,0,len(nums)-1)
    r = find_last(nums,target,l,len(nums)-1)
    return l,r

def find_ir(nums,bg,ed):
    if bg>ed:
        return -1
    mid = (bg+ed)//2
    if nums[mid]>mid:
        if mid>0 and nums[mid-1]==mid-1 or mid == 0:
            return mid
        else:
            return find_ir(nums,bg,mid-1)
    elif nums[mid]==mid:
        return find_ir(nums,mid+1,ed)
    else:
        return find_ir(nums,bg,mid-1)

def find_nn(nums):
    def helper(nums,bg,ed):
        if bg>ed:
            return -1
        mid = (bg+ed)//2
        if nums[mid] == mid:
            return mid
        elif nums[mid]>mid:
            return helper(nums,bg,mid-1)
        else:
            return helper(nums,mid+1,ed)
    tmp = []
    out = []
    a = helper(nums,0,len(nums)-1)
    for i in range(a-1,-1,-1):
        if nums[i]==i:
            tmp.append(i)
        else:
            break
    for i in range(len(tmp)):
        out.append(tmp.pop())
    for i in range(a,len(nums)):
        if nums[i]==i:
            out.append(i)
        else:
            break
    return out


if __name__ == '__main__':
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 1))
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 2))
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 3))
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 4))
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 5))
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 6))
    print(times_in_sort([1, 2, 3, 4, 4, 5, 6, 7], 7))
    nums = [0,1,2,4,5,6]
    nums = [1,2,3]
    print(find_ir(nums,0,len(nums)-1))
    nums = [-3,-1,2,3,4,6,8,9]
    print(find_nn(nums))