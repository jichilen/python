def re_match(str1, tmplate):
    if len(str1) == 0 and len(tmplate) == 0:
        return True
    elif len(str1) == 0:
        if len(tmplate)&1==1:
            return False
        for i in range(len(tmplate)-1,0,-2):
            if tmplate[i] !='*':
                return False
        return True
    elif len(tmplate)==0:
        return False

    if tmplate[-1] == '*':
        if tmplate[-2] == str1[-1] or tmplate[-2] == '.':
            return re_match(str1, tmplate[:-2]) \
                   or re_match(str1[:-1], tmplate[:-2]) \
                   or re_match(str1[:-1], tmplate)
        else:
            return re_match(str1, tmplate[:-2])
    elif tmplate[-1] == '.' or tmplate[-1] == str1[-1]:
        return re_match(str1[:-1], tmplate[:-1])
    else:
        return False



if __name__ == '__main__':
    str1 = 'aaa'
    tmplate = 'a.aa'
    print(re_match(str1, tmplate))
