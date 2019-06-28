def count_one(num):
    out = 0
    if num<0:
        num *=-1
        out+=1
    while num:
        if num&1==1:
            out+=1
        num = num>>1
    return out

if __name__ == '__main__':
    print(count_one(-9))