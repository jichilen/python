from sympy import Symbol,solve,sqrt
from PIL import Image
import numpy
def nearest_plane(p,planes):
    # planes[4]:[{A: 0, B: -1/5, D: 0}, {A: 1/5, B: 0, D: -2}, {A: 0, B: 1/5, D: -2}, {A: -1/5, B: 0, D: 0}]
    plane_i=0
    min_dist=10000000000000000000000
    for idx,plane in enumerate(planes):
        a=plane[0]
        b=plane[1]
        d=plane[2]
        dist=abs(a*p[0]+b*p[1]+p[2]+d)/sqrt(a*a+b*b+1)
        if dist<min_dist:
            plane_i=idx
            min_dist=dist
    return plane_i

def RLS(G):
    # G :{0:[pi,p2,..],1:[],...}  p1=[x,y,z]
    new_plane=[]
    for idx,_ in enumerate(G):
        points=G[idx]
        a0 = Symbol('a0')
        a1 = Symbol('a1')
        a2 = Symbol('a2')
        xi_squr=sum([i[0]*i[0] for i in points])
        xi=sum([i[0] for i in points])
        xi_yi=sum([i[0]*i[1] for i in points])
        xi_zi = sum([i[0] * i[2] for i in points])
        yi_squr = sum([i[1]*i[1] for i in points])
        yi = sum([i[1] for i in points])
        yi_zi=sum([i[1]*i[2] for i in points])
        zi=sum([i[2] for i in points])
        n=len(points)

        tm=[]
        tm.append(solve([a0 * xi_squr + a1 * xi_yi + a2 * xi - xi_zi, a0 * xi_yi + a1 * yi_squr + a2 *yi - yi_zi, a0 * xi + a1 * yi + a2*n - zi], [a0, a1, a2]))

        print(tm[0][a0],tm[0][a1],tm[0][a2])

        A=tm[0][a0]*(-1)
        B=tm[0][a1]*(-1)
        D=tm[0][a2]*(-1)

        new_plane.append([A,B,D])
    return new_plane#,residual

def plane_cluster(points,bbox):
    x_center=sum([p[0] for p in points])/len(points)
    y_center=sum([p[1] for p in points])/len(points)
    z_center=1
    xa,ya,xb,yb,xc,yc,xd,yd=bbox[0],bbox[1],bbox[2],bbox[3],bbox[4],bbox[5],bbox[6],bbox[7]
    A = Symbol('A')
    B = Symbol('B')
    D = Symbol('D')
    '''
    A * xa + B * ya + 0 + D = 0
    A * xb + B * yb + 0 + D = 0
    A * x_center + B * y_center + z_center + D = 0
    '''
    planes=[]
    tm=[]
    tm.append(solve([A * xa + B * ya + 0 + D, A * xb + B * yb + 0 + D, A * x_center + B * y_center + z_center + D],
                        [A, B, D]))
    tm.append(solve([A * xb + B * yb + 0 + D, A * xc + B * yc + 0 + D, A * x_center + B * y_center + z_center + D],
                        [A, B, D]))
    tm.append(solve([A * xc + B * yc + 0 + D, A * xd + B * yd + 0 + D, A * x_center + B * y_center + z_center + D],
                        [A, B, D]))
    tm.append(solve([A * xd + B * yd + 0 + D, A * xa + B * ya + 0 + D, A * x_center + B * y_center + z_center + D],
                        [A, B, D]))
    for i in range(0,4):
        a = tm[i][A]
        b = tm[i][B]
        d = tm[i][D]
        planes.append([a,b,d])
    print(planes)

    max_iter=10
    iter=0
    while iter<max_iter :
        G={}
        G[0]=[]
        G[1]=[]
        G[2]=[]
        G[3]=[]
        for p in points:
            plane_i=nearest_plane(p,planes)
            G[plane_i].append(p)
        planes=RLS(G)
        iter+=1
    return planes

'''
im=Image.open('0_mask.png')
im_array=numpy.array(im)
amin, amax = 0, 255 # 求最大最小值
im_array = im_array/(amax-amin)
#print(im_array)
points=[]
for idx,i in enumerate(im_array):
    for jdx,j in enumerate(i):
        points.append([idx,jdx,j])
bbox=[0,0,27,0,27,27,0,27]
planes=plane_cluster(points,bbox)
print(planes)
'''

import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

#创建一个Axes3d对象
fig=plt.figure()
ax=Axes3D(fig)

#x，y的取值返回是从-5到+5，每隔0.25取一个点
x=np.arange(0,50,1)
y=np.arange(0,50,1)

#[X,Y] = meshgrid(x,y) 将向量x和y定义的区域转换成矩阵X和Y，
#这两个矩阵可以用来表示mesh和surf的三维空间点以及两个变量的赋值。
#其中矩阵X的行向量是向量x的简单复制，而矩阵Y的列向量是向量y的简单复制。
x,y=np.meshgrid(x,y)
#r=np.sqrt(x**2+y**2)
#z=np.sin(r)
#z=x**2+y**2
planes=[[-0.00683187460238299, -0.0816337067121229, 0.162890261750164], [0.0700874159910236, 0.000274830370526055, -1.89742954148067], [-0.0102802908808784, 0.0578588231710164, -1.32668739343541], [-0.0745250847057818, -0.000174448944908593, 0.0438096199551639]]
for idx,i in enumerate(planes):
    a=i[0]
    b=i[1]
    d=i[2]
    z=(-1)*a*x-b*y-d
    if  idx==2:
        continue

    #break
    #plot_surface 是绘制一个平面 ax.scatter 是绘制点
    surf=ax.plot_surface(x,y,z)
ax.set_zlim(0, 5)
plt.show()


'''
bbox=[0,0,10,0,10,10,0,10]
x_center=5
y_center=5
z_center=1
xa,ya,xb,yb,xc,yc,xd,yd=bbox[0],bbox[1],bbox[2],bbox[3],bbox[4],bbox[5],bbox[6],bbox[7]
A = Symbol('A')
B = Symbol('B')
D = Symbol('D')
planes=[]

planes.append(solve([A * xa + B * ya + 0 + D, A * xb + B * yb + 0 + D,A * x_center + B * y_center + z_center + D ],[A, B, D]))
planes.append(solve([A * xb + B * yb + 0 + D, A * xc + B * yc + 0 + D, A * x_center + B * y_center + z_center + D],[A, B, D]))
planes.append(solve([A * xc + B * yc + 0 + D, A * xd + B * yd + 0 + D, A * x_center + B * y_center + z_center + D],[A, B, D]))
planes.append(solve([A * xd + B * yd + 0 + D, A * xa + B * ya + 0 + D, A * x_center + B * y_center + z_center + D],[A, B, D]))
print(planes)
'''
