class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0:return True
        if x + y < z:
            return False
        if x>y:
            x,y=y,x
        while x!=0:
            x,y = y%x,x
        if y == 0:return False
        return z%y==0



if __name__ == '__main__':
    so = Solution()
    print(so.canMeasureWater(3,5,4))