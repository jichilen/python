def item_of_numlist(n):
    if n<10:
        return n
    base = 10
    frac = 1
    while n >= base:
        last_base = base
        base = base + (frac+1)*pow(10,frac)*9
        frac+=1
    over = n -last_base
    bi = over % frac
    pas = over //frac
    return str(pow(10,frac-1)+pas)[bi]

if __name__ == '__main__':
    for i in range(100):
        print(item_of_numlist(i))
