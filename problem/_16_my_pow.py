def my_pow(num, exponent):
    flag = 0
    if exponent < 0:
        exponent *= -1
        flag = 1
    out = pow_helper(num,exponent)
    if flag:
        if out:
            return 1/out
        return None
    return out

def pow_helper(num, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return num
    fractor = num if exponent & 1 == 1 else 1
    out = pow_helper(num, exponent >> 1)
    return out * out * fractor


if __name__ == '__main__':
    num = 2
    exponent = 12
    print(my_pow(num, exponent))
    exponent = -1
    print(my_pow(num, exponent))
