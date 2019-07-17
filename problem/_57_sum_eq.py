def sum_eq(nums,target):
    dic = {}
    for t in nums:
        if t in dic:
            return [t,dic[t]]
        dic[target-t] = t

def sum_seq_eq(target):
    p1 = 1
    p2 = 1
    out = []
    su = 1
    while p2<target/2+1:
        # su=(p1+p2)*(p2-p1+1)/2
        if su<target:
            p2+=1
            su+=p2
        elif su == target:
            out.append([p1,p2])
            p2+=1
            su+=p2
        else:
            su-=p1
            p1+=1
    return out



if __name__ == '__main__':
    print(sum_eq([1,2,4,7,11,15],15))
    print(sum_seq_eq(15))