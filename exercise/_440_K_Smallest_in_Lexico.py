from functools import cmp_to_key


class Solution:
    def findKthNumber(self, n: int, m: int) -> int:
        i = 1
        m -= 1
        while (m != 0):
            low = i
            high = i + 1
            num = 0
            while (low <= n):
                num += min(n + 1, high) - low;
                low *= 10;
                high *= 10;
            if (num > m):
                i *= 10;
                m -= 1
            else:
                m -= num;
                i += 1
        return i

    def findKthNumber1(self, n: int, k: int) -> int:
        if n <= 0:
            return None
        if k <= 0: return None
        n = n + 1
        k = k - 1

        def mysort(a, b):
            a = str(a)
            b = str(b)
            if a < b:
                return -1
            if a == b:
                return 0
            return 1

        out = list(range(1, n))
        out = sorted(out, key=cmp_to_key(mysort))
        print(out)
        return out[k]


if __name__ == '__main__':
    so = Solution()
    print(so.findKthNumber1(200, 120))
