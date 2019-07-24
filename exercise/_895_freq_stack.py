import collections
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x


# class FreqStack:
#
#     def __init__(self):
#         self.fstack = []
#         self.freqdic = {}
#         self.len = 0
#
#     def push(self, x: int) -> None:
#         self.fstack.append(x)
#         self.len +=1
#         if x in self.freqdic:
#             self.freqdic[x]+=1
#         else:
#             self.freqdic[x]=1
#
#     def pop(self) -> int:
#         maxl = -1
#         maxk = []
#         for k,v in self.freqdic.items():
#             if v>maxl:
#                 maxl = v
#                 maxk = [k]
#             elif v==maxl:
#                 maxk.append(k)
#         if maxl ==-1:return None
#         tmp = []
#         while 1:
#             ttmp = self.fstack.pop()
#             if ttmp in maxk:
#                 self.freqdic[ttmp]-=1
#                 break
#             tmp.append(ttmp)
#         for it in tmp[::-1]:
#             self.fstack.append(it)
#         return ttmp
#
#
#     def printl(self):
#         print(self.fstack)

if __name__ == '__main__':
    a=["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "push", "pop", "push", "pop", "push", "pop",
     "push", "pop", "pop", "pop", "pop", "pop", "pop"]
    b=[[], [7], [6], [2], [6], [3], [3], [], [2], [], [2], [], [5], [], [6], [], [], [], [], [], []]
    obj = FreqStack()
    for fun, arg in zip(a[1:], b[1:]):
        getattr(obj, fun)(*arg)
        obj.printl()