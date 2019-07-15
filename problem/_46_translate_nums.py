def tran(num):
    num = int(num)
    if num<0:
        return None
    if num>25:
        return None
    return chr(ord('a')+num)

def translate_nums(nums):
    def helper(nums):
        if len(nums)<=0:
            return []
        if len(nums)==1:
            return [tran(nums)]
        out = []
        st = tran(nums[:1])
        tmp = helper(nums[1:])
        for a in tmp:
            b= st+a
            out.append(b)
        st = tran(nums[:2])
        tmp = helper(nums[2:])
        for a in tmp:
            b = st + a
            out.append(b)
        return out
    nums = str(nums)
    return  helper(nums)


if __name__ == '__main__':
    nums = 12258
    print(translate_nums(nums))
