def sort_ugly_number(n):
    out = [1]
    p2=0;p3=0;p5=0
    while len(out)<n:
        r2 = out[p2]*2
        r3 = out[p3]*3
        r5 = out[p5]*5
        mo = min(r2,r3,r5)
        out.append(mo)
        if mo == r2:
            p2+=1
        if mo == r3:
            p3+=1
        if mo == r5:
            p5+=1
    return out[n-1]

if __name__ == '__main__':
    print(sort_ugly_number(1500))