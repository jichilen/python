def dice_prob(n,k):
    pre = [0]
    pre.extend([1 for _ in range(k)])
    if n == 1:
        return pre
    for i in range(1,n):
        out = [0 for _ in range(k*(i+1)+1)]
        for j in range(len(out)):
            for l in range(k):
                if j-l-1<0 or j-l-1>len(pre)-1:
                    continue
                out[j]+=pre[j-l-1]
        pre = out
    return pre

if __name__ == '__main__':
    print(dice_prob(11,6))



