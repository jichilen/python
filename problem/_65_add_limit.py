def add_limit(n1,n2):
    c = 0
    while n2!=0 and c<32:
        s = n1^n2
        p = n1&n2
        n1 = s
        n2 = p<<1
        c+=1
    return n1&0xffffffff


if __name__ == '__main__':
    print(add_limit(13,7))