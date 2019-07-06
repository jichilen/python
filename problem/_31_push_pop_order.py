
def push_pop_order(inseq,outseq):
    if len(inseq) != len(outseq):return False
    tmp = []
    pin = 0
    pout = 0
    while 1:
        if pin<len(inseq) and inseq[pin] == outseq[pout]:
            pin+=1
            pout+=1
        else:
            if len(tmp)>0 and tmp[-1]==outseq[pout]:
                tmp.pop()
                pout+=1
            else:
                if pin >= len(inseq):
                    return False
                tmp.append(inseq[pin])
                pin+=1
        if pout == len(outseq):
            return True

if __name__ == '__main__':
    inseq = [1,2,3,4,5]
    outseq = [4,5,3,2,1]
    print(push_pop_order(inseq,outseq))
    outseq = [4, 3, 5, 2, 1]
    print(push_pop_order(inseq, outseq))
    outseq = [4, 3, 5, 1, 2]
    print(push_pop_order(inseq, outseq))
    outseq = [1, 2, 3, 5, 4]
    print(push_pop_order(inseq, outseq))