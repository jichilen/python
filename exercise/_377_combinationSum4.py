from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        tmp = [0]*(target+1)
        for n in nums:
            if n <= target:
                tmp[n]=1
        for i in range(target+1):
            for n in nums:
                if i-n>0:
                    tmp[i] = tmp[i-n]+tmp[i]
        return tmp[-1]



    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        finddic = {target:[[]]}
        out = []
        while len(finddic)>0:
            tmpdic = {}
            for k,lists in finddic.items():
                if k == 0:
                    out.extend(lists)
                for n in nums:
                    if k-n>=0:
                        for l in lists:
                            l = l.copy()
                            l.append(n)
                            if k-n in tmpdic:
                                tmpdic[k-n].append(l)
                            else:
                                tmpdic[k-n]=[l]
            finddic = tmpdic
        return out

if __name__ == '__main__':
    so = Solution()
    print(so.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],10))