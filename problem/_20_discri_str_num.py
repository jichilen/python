def discrio_str_num(str1):
    p = 0
    strlen = len(str1)
    numdigit = 0
    if strlen==0:
        return False
    num = '0123456789'
    if p<strlen and str1[p] in '+-':
        p+=1
    while p<strlen and str1[p] in num:
        p+=1
        numdigit+=1
    if p<strlen and str1[p] == '.':
        p+=1
    while p<strlen and str1[p] in num:
        p += 1
        numdigit += 1
    if numdigit==0:
        return False
    if p<strlen and str1[p] in 'Ee':
        p+=1
        if p<strlen and str1[p] in '+-':
            p+=1
        if p == strlen:
            return False
    while p<strlen and str1[p] in num:
        p += 1
        numdigit += 1
    if p == len(str1):
        return True
    return False

if __name__ == '__main__':
    str1 = '+1.231E12'
    print(discrio_str_num(str1))
    str1 = '-.231E12'
    print(discrio_str_num(str1))
    str1 = '+E12'
    print(discrio_str_num(str1))
    str1 = '+1.12'
    print(discrio_str_num(str1))
    str1 = '3212'
    print(discrio_str_num(str1))
    str1 = '+100'
    print(discrio_str_num(str1))
    str1 = '5e2'
    print(discrio_str_num(str1))
    str1 = '-123'
    print(discrio_str_num(str1))
    str1 = '3.1416'
    print(discrio_str_num(str1))
    str1 = '-1e-16'
    print(discrio_str_num(str1))
    print()
    str1 = '12e'
    print(discrio_str_num(str1))
    str1 = '1a314'
    print(discrio_str_num(str1))
    str1 = '1.2.3'
    print(discrio_str_num(str1))
    str1 = '+-5'
    print(discrio_str_num(str1))
    str1 = '12e+5.6'
    print(discrio_str_num(str1))