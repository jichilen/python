from typing import List
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        def parti(A,bg,ed):
            if bg>=ed: return bg
            mid = (bg+ed)//2
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid]>A[mid-1]:
                return parti(A,mid+1,ed)
            elif A[mid]>A[mid+1]:
                return parti(A,bg,mid)
        if len(A)<3:
            return None
        return parti(A,0,len(A))

if __name__ == '__main__':
    A=[0,1,2,1,2,3,1]
    so = Solution()
    print(so.peakIndexInMountainArray(A))