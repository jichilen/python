Fun = {True:None,
       False:None}

def sum_0(n):
    return 0

def sum_1(n):
    return Fun[n!=0](n-1)+n



if __name__ == '__main__':
    Fun[True] = sum_1
    Fun[False] = sum_0
    print(sum_1(10))