class Solution:
    def findCheapestPrice(self, n: int, flights  , src: int, dst: int, K: int) -> int:
        MAX = 9999999
        detmap = [MAX]*n
        detmap[src] = 0
        lastdet = detmap.copy()
        for i in range(K+1):
            for flight in flights:
                if lastdet[flight[0]]!=MAX:
                    detmap[flight[1]]=min(flight[2]+lastdet[flight[0]],detmap[flight[1]])
            for j in range(n):
                lastdet[j]=detmap[j]
        return detmap[dst] if detmap[dst]!=MAX else -1



if __name__ == '__main__':
    n=4
    flights=[[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src=0
    dst=3
    K=1
    so = Solution()
    print(so.findCheapestPrice(n, flights, src, dst, K))