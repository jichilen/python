'''
什么时候使用动态规划：
    最优解，可分解，子问题的最优解能得到整个问题的最优解
    子问题有相互重叠的部分，也就是说通常需要用带记忆的递归来求解
'''
def cut_rope(n):
    mem = []
    for i in range(n+1):
        if i<2:
            mem.append(1)
        else:
            out =0
            for j in range(1,i//2+1):
                out =max(out,mem[j]*mem[i-j],i)
            mem.append(out)
    print(mem)
    return mem[-1]


if __name__ == '__main__':
    cut_rope(10)