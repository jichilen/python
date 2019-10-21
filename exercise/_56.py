from typing import  List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==0:return []
        intervals.sort(key=lambda x:x[0])
        out = []
        bgind = 0
        maxr = intervals[bgind][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]>maxr:
                out.append([intervals[bgind][0],maxr])
                bgind = i
                maxr = intervals[bgind][1]
            maxr = max(maxr,intervals[i][1])
        out.append([intervals[bgind][0],maxr])
        return out