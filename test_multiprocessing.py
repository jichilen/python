from multiprocessing import Process,Manager


def change_v(l):
    tmp = l[1]
    tmp.append(2)
    l[1]=tmp
    l[2]=[2]

def change_c(l):
    l[1].append(2)
    l[2]=[2]


if __name__ == '__main__':
    a=Manager().dict()
    a[1]=[1]
    p = Process(target=change_c,args=(a,))
    p.start()
    p.join()
    print(a)