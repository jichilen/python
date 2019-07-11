def count_one_in_vec(n):
    if n<=0:return 0
    n=str(n)
    def helper(n_s):
        if len(n_s)==0:
            return 0
        cal = 0
        if n_s[0] == '1':
            cal+=int(n_s[1:])
        else:
            cal+=pow(10,len(n_s)-1)
        if len(n_s)>=2:
            cal+=pow(10,len(n_s)-2)*int(n_s[0])*(len(n_s)-1)
        out = helper(n_s[1:])
        return out+cal
    return helper(n)

if __name__ == '__main__':
    print(count_one_in_vec(10))
    print(count_one_in_vec(5))
    print(count_one_in_vec(45))
    print(count_one_in_vec(345))
    print(count_one_in_vec(1345))
    print(count_one_in_vec(21345))
    print(count_one_in_vec(0))
    print(count_one_in_vec(-1))
    print(count_one_in_vec(99))