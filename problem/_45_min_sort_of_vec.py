import functools
def min_sort_of_vec(nums):
    if len(nums)==0:
        return []

    return sorted(nums,key=functools.cmp_to_key(compare_two_num))

def compare_two_num(n1,n2):
    n1 = str(n1)
    n2 = str(n2)
    if n1>n2:
        return -1
    elif n1==n2:
        return 0
    else:
        return 1

if __name__ == '__main__':
    nums = [321,32,3]
    print(min_sort_of_vec(nums))