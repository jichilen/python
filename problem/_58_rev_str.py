def rev_str(strs):
    st = strs.split(' ')
    return ' '.join(st[::-1])

def rev_str1(strs):
    def rev(strs,bg,ed):
        while bg<ed:
            strs[bg],strs[ed] =strs[ed],strs[bg]
            bg += 1
            ed -= 1
    rev(strs,0,len(strs)-1)
    lasts = 0
    for i,t in enumerate(strs):
        if t == ' ':
            rev(strs,lasts,i-1)
            lasts = i+1

def rev_str2(strs,tar):
    def rev(strs,bg,ed):
        while bg<ed:
            strs[bg],strs[ed] =strs[ed],strs[bg]
            bg += 1
            ed -= 1
    rev(strs,0,tar-1)
    rev(strs,tar,len(strs)-1)
    rev(strs,0,len(strs)-1)

if __name__ == '__main__':
    strs = "I am a student."
    print(rev_str(strs))
    strs = [i for i in strs]
    rev_str1(strs)
    print(strs)
    strs1 = "abcdefg"
    strs1 = [i for i in strs1]
    rev_str2(strs1,2)
    print(strs1)