def no_duplicate(strs):
    l = len(strs)
    if l == 0:return 0
    out = [0 for _ in range(l+1)]
    for i in range(l):
        last = -1
        for j in range(i-1,-1,-1):
            if strs[j] == strs[i]:
                last = j
                break
        if last<0 or i-last>out[i]:
            out[i+1] = out[i]+1
        else:
            out[i+1] = i - last
    return max(out)



if __name__ == '__main__':
    strs = 'arabcacfr'
    print(no_duplicate(strs))
    print(no_duplicate(''))
    print(no_duplicate('aaaaa'))
    print(no_duplicate('aavsdfasdgasdfasdgasd'))