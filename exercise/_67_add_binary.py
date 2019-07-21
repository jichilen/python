class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_help(a, b):
            if a == '0':
                return '0', b
            if a == '1' and b == '1':
                return '1', '0'
            else:
                return '0', '1'

        if len(a) > len(b):
            a, b = b, a
        l = len(b)
        i = 0
        out = ['0'] * l
        update = '0'
        while i < l:
            if i >= len(a):
                update, out[l - i - 1] = add_help(b[l - i - 1], update)
            else:
                tmp, out[l - i - 1] = add_help(b[l - i - 1], update)
                update, out[l - i - 1] = add_help(out[l - i - 1], a[len(a) - 1 - i])
                update = max(tmp,update)
            i += 1
        if update=='1':
            return update+''.join(out)
        return ''.join(out)

if __name__ == '__main__':
    so = Solution()
    print(so.addBinary('0','0'))