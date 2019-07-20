def multi_without_div(nums):
    if len(nums)==0:return []
    B=[1]
    C=[1]
    for i in range(len(nums)-1):
        j=len(nums)-1-i
        B.append(B[i]*nums[i])
        C.append(C[i]*nums[j])
    for i in range(len(nums)):
        B[i]*=C[len(nums)-i-1]
    return B



if __name__ == '__main__':
    nums = list(range(1,10))
    print(multi_without_div(nums))
    a=1000
    b=1000
    print(a is b)