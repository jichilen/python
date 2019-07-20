from multiprocessing import Process,Manager
import multiprocessing
from time import time
def change_v(l):
    tmp = l[1]
    tmp.append(2)
    l[1]=tmp
    l[2]=[2]

def change_c(l):
    l[1].append(2)
    l[2]=[2]

def change_A(A):
    A.value+=1
    print(A.value)

def change_B(A):
    print(A+1)

if __name__ == '__main__':
    a=Manager().dict()
    a[1]=[1]
    p = Process(target=change_c,args=(a,))
    p.start()
    p.join()
    print(a)
    #####
    s=Manager().Value('d',1)
    p = multiprocessing.Pool(4)
    # s=1
    t=time()
    for _ in range(10):
        p.apply_async(change_A,args=(s,))
    p.close()
    p.join()
    print(time()-t)
