class Solution:
    def lastSubstring(self, s: str) -> str:
        c = max(s)
        length = len(s)
        heads, lheads = [], 0
        for i in range(length):
            if s[i] != c:
                continue
            if i == 0 or s[i-1] != c:
                heads.append(i)
                lheads += 1

        tmp = s[heads[0]:]
        ans = heads[0]
        for i in range(1, lheads):
            if i == lheads - 1:
                cur = s[heads[i]:]
            else:
                cur = s[heads[i]:heads[i+1]]
            if tmp < cur:
                tmp = cur
                ans = heads[i]

        return s[ans:]
        # while len(maxind)>1:
        #     tmp = [maxind[0]]
        #     for k in range(1,len(maxind)):
        #         if maxind[k]+j<len(s):
        #             if s[maxind[k]+j] == s[tmp[0]+j]:
        #                 tmp.append(maxind[k])
        #             elif s[maxind[k]+j] > s[tmp[0]+j]:
        #                 tmp = [maxind[k]]
        #     maxind = tmp
        #     j+=1


if __name__ == '__main__':

    so = Solution()
    print(so.lastSubstring('baaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaa'))