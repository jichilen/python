class Solution:
    def fullJustify(self, words, maxWidth: int):
        lens = [len(st) for st in words]
        def word_in_line(words,lens):
            outl = []
            tmp = []
            lcal = 0
            for i in range(len(words)):
                if lcal+lens[i]>maxWidth:
                    tmp.append(lcal-1)
                    outl.append(tmp)
                    tmp=[]
                    lcal=0
                tmp.append(words[i])
                lcal=lcal+lens[i]+1
            tmp.append(lcal-1)
            outl.append(tmp)
            return outl
        outl = word_in_line(words,lens)
        out = []
        for word_l in outl[:-1]:
            num_s = maxWidth-word_l.pop()
            num_w = len(word_l)
            tmp = word_l[0]
            if num_w<=1:
                out.append(tmp+' '*num_s)
                continue
            d,m = divmod(num_s,num_w-1)
            for i in range(1,num_w):
                l_s=d+1
                if i<=m:
                    l_s+=1
                tmp = tmp+' '*l_s+word_l[i]
            out.append(tmp)
        word_l = outl[-1]
        num_s = maxWidth - word_l.pop()
        out.append(' '.join(word_l)+' '*(num_s))
        return out


if __name__ == '__main__':
    str=["What", "must", "be", "acknowledgment", "shall", "be"]
    num=16
    so=Solution()
    out = so.fullJustify(str,num)
    for x in out:
        print(x)