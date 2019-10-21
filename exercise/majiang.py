class majiang():
    def __init__(self):
        self.num = 9

    def tri(self,status):
        if sum(status) == 0:
            return True
        tri_sta = []
        for i in range(self.num):
            if status[i]>=3:
                tri_sta.append([i,i,i])
        for i in range(1,len(status)-1):
            if status[i-1]>0 and status[i]>0 and status[i+1]>0:
                tri_sta.append([i-1,i,i+1])

        if not tri_sta:
            return False
        else:
            for tri_s in tri_sta:
                for i in tri_s:
                    status[i]-=1
                if self.tri(status):
                    return True
                for i in tri_s:
                    status[i]+=1

    def win(self,nums):
        status = [0]*self.num
        double_s = []
        for n in nums:
            status[n-1]+=1
            if status[n-1]==2:
                double_s.append(n-1)
            if status[n-1]>4:
                return False
        for ds in double_s:
            status[ds]-=2
            if self.tri(status):
                return True
            status[ds]+=2
        return False
    
    

    def miss(self,nums):
        out = []
        for i in range(self.num):
            nums.append(i+1)
            if self.win(nums):
                out.append(i+1)
            nums.pop()
        return out


if __name__ == '__main__':
    ma = majiang()
    nums = [1,1,1,1,2,3,4,5,3,4,5,6,7]
    print(sorted(nums))
    print(ma.miss(nums))