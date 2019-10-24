def count_one(num):
    out = 0
    if num < 0:
        num *= -1
        out += 1
    while num:
        if num & 1 == 1:
            out += 1
        num = num >> 1
    return out


def count_one1(n):
    return sum([(n >> i & 1) for i in range(0, 32)])


def count_one2(num):
    out = 0
    if num < 0:
        num = num&0xffffffff
    while num!=0:
        out +=1
        num = num&(num-1)
    return out


if __name__ == '__main__':
    print(count_one(-1))
    print(count_one1(-1))
