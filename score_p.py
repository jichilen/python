# -*- coding: utf8 -*-
# import math
import numpy as np
import cv2
import time
import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage.util import random_noise
# from sympy import Symbol,solve
# from scipy.optimize import leastsq
# from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
# import scipy.linalg as sl


# class batch_provider():
#     def __init__(self, data, batch_size):
#         # data   list[n*d]
#         self.batch_size = batch_size
#         self.data = data
#         self.len = [len(d) for d in data]
#         self.idx = [0] * len(data)
#
#     def get(self):
#         while 1:
#             for i, id in enumerate(self.idx):
#                 if id + self.batch_size > self.len[i] - 1:
#                     self.idx[i] = self.len[i] - 1 - self.batch_size - id
#             data_o = []
#             for i in range(len(self.data)):
#                 if self.idx[i] < 0:
#                     da = np.vstack([self.data[i][self.idx[i]:, :], self.data[i] \
#                         [:self.idx[i] + self.batch_size, :]])
#                 else:
#                     da = self.data[i][self.idx[i]:self.idx[i] + self.batch_size, :]
#                 data_o.append(da)
#                 self.idx[i] += self.batch_size
#             yield (data_o)
def score_cal(i_h, i_w, annos):
    if not isinstance(annos, list):
        annos = [annos]
    score = np.zeros((i_h, i_w))
    for anno in annos:
        anno = np.array(anno).reshape(-1, 2).astype(np.int32)
        assert anno.size == 8
        maxx, maxy = np.max(anno, 0)
        minx, miny = np.min(anno, 0)
        xo,yo=np.mean(anno,0)
        c = np.array([xo,yo])
        xp = np.arange(minx,maxx)
        yp = np.arange(miny,maxy)
        xp,yp = np.meshgrid(xp,yp)
        xy = np.hstack((xp.reshape(-1,1),yp.reshape(-1,1)))
        planes = np.hstack((anno,anno[[-1,0,1,2]]))
        z = []
        for plane in planes:
            LM = np.hstack([plane, c])
            LM = LM.reshape(-1, 2)
            LM = np.hstack([LM, np.array([[1], [1], [1]])])
            vplane=np.dot(np.linalg.inv(LM), np.array([0, 0, 1]))
            z.append(np.dot(np.hstack((xy,np.ones((xy.shape[0],1)))),vplane))
        z=np.min(np.array(z),0).clip(0)
        z=np.reshape(z,(maxy-miny,maxx-minx))
        score[miny:maxy,minx:maxx]=z
    return score

def score_cal_old(i_h, i_w, annos):
    if not isinstance(annos, list):
        annos = [annos]
    score = np.zeros((i_h, i_w))
    for anno in annos:
        anno = np.array(anno).reshape(-1, 2).astype(np.int32)
        assert anno.size == 8
        maxx, maxy = np.max(anno, 0)
        minx, miny = np.min(anno, 0)
        # xo,yo=np.mean(anno,0)
        anno = anno.reshape(-1)
        xa, ya, xb, yb, xc, yc, xd, yd = anno[0], anno[1], anno[2], anno[3], anno[4], anno[5], anno[6], anno[7]
        xo = (xa + xb + xc + xd) / 4
        yo = (ya + yb + yc + yd) / 4
        for xp in range(minx, maxx + 1):
            for yp in range(miny, maxy + 1):
                if IsInside(xp, yp, xo, yo, xa, ya, xb, yb):
                    xm, ym, xn, yn = xa, ya, xb, yb
                elif IsInside(xp, yp, xo, yo, xb, yb, xc, yc):
                    xm, ym, xn, yn = xb, yb, xc, yc
                elif IsInside(xp, yp, xo, yo, xc, yc, xd, yd):
                    xm, ym, xn, yn = xc, yc, xd, yd
                elif IsInside(xp, yp, xo, yo, xa, ya, xd, yd):
                    xm, ym, xn, yn = xa, ya, xd, yd
                else:
                    continue
                ta = np.linalg.inv(np.array([[xm - xo, xn - xo], [ym - yo, yn - yo]]))
                tb = np.array([xp - xo, yp - yo])
                alpha_beta = np.dot(ta, tb)
                score[yp, xp] = max(1 - (alpha_beta[0] + alpha_beta[1]), 0)
    return score


def IsTrangleOrArea(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def IsInside(x, y, x1, y1, x2, y2, x3, y3):
    # 三角形ABC的面积
    ABC = IsTrangleOrArea(x1, y1, x2, y2, x3, y3)
    # 三角形PBC的面积
    PBC = IsTrangleOrArea(x, y, x2, y2, x3, y3)
    # 三角形ABC的面积
    PAC = IsTrangleOrArea(x1, y1, x, y, x3, y3)
    # 三角形ABC的面积
    PAB = IsTrangleOrArea(x1, y1, x2, y2, x, y)
    return (ABC == PBC + PAC + PAB)


#######
# 分界线
#######
# def tttttest(scores):
#     G, vplanes = plane_cluster(scores)
#     for iiii in range(4):
#         g = np.array(G[iiii])
#         plane = vplanes[iiii]
#         u = np.mean(g, 0)
#         v = np.std(g, 0)
#         g = (g - u) / v
#         num_planes = 1
#         A = torch.zeros(num_planes, requires_grad=True)
#         B = torch.zeros(num_planes, requires_grad=True)
#         D = torch.zeros(num_planes, requires_grad=True)
#         i = 0
#         while i < 1000:
#             i += 1
#             loss = RLS(torch.FloatTensor([g]), A, B, D)
#             res = sum(loss) / len(g)
#             res.backward(retain_graph=True)
#             for d in [A, B, D]:
#                 update(d, 0.01)
#         with torch.no_grad():
#             fig = plt.figure()
#             ax = Axes3D(fig)
#             z = A.data.numpy() * g[:, 0] + B.data.numpy() * g[:, 1] + D.data.numpy()
#             # ax.plot_surface(x, y, z)
#             ax.plot_trisurf(g[:, 0], g[:, 1], z)
#             # poly3d=[[x,y,0],[]]
#             # ax.add_collection3d(Poly3DCollection(poly3d, facecolors='w', linewidths=1, alpha=0.3))
#             ax.scatter3D(g[:, 0], g[:, 1], g[:, 2])
#         plt.show()


def plane_cluster(scores):
    # init
    h, w = scores.shape
    idy, idx = np.where(scores > 0.1)
    ids = scores[idy, idx]
    P = np.hstack([idx[:, None], idy[:, None], ids[:, None]])
    N = len(P)
    idy, idx = np.where(scores > 0.6)
    c = np.mean(np.hstack([idx[:, None], idy[:, None]]), 0)
    # c = np.mean(P[:,:2],0)
    c = np.around(c, decimals=4)
    box = np.array([[0, 0], [w, 0], [w, h], [0, h]])

    planes = np.hstack([box, np.vstack([box[1:], box[0]])])
    ####
    # return near_plane(P, c, planes)
    ####
    num_planes = 4
    res_th = 0.15
    lr = 0.01
    vis = False

    # iter
    A = torch.zeros(num_planes, requires_grad=True)
    B = torch.zeros(num_planes, requires_grad=True)
    D = torch.zeros(num_planes, requires_grad=True)
    for itera in range(10):
        i = 0
        res = 999
        G, vplanes = near_plane(P, c, planes)
        # gaussian normalize
        u = [np.mean(g, 0) for g in G]
        v = [np.std(g, 0) for g in G]
        # normalize to [0-1]
        # gm = np.max(np.concatenate(G), 0)
        # gm = torch.FloatTensor([np.max(g, 0) for g in G])
        G = [(G[i] - u[i]) / v[i] for i in range(len(G))]
        if itera==0:
            # a large lr for the first iteration to get a good init state
            lr=0.5
            # # use LSE to init(too slow)
            # # n_p = torch.FloatTensor(LSE(G))
            # # cal the abd of the plane
            # # use plane or random sample points to init(too slow)
            # Rs = []
            # for id, plane in enumerate(planes):
            #     LM = np.hstack([plane, c])
            #     LM = LM.reshape(-1, 2)
            #     LM = np.hstack([LM, np.array([[0], [0], [1]])])
            #     # randid=np.random.randint(0,len(G[id]),3)
            #     # LM = G[id][randid]
            #     re_xyz = (LM - u[id])/v[id]
            #     LM = np.hstack([re_xyz[:,:2], np.array([[1], [1], [1]])])
            #     R = np.dot(np.linalg.inv(LM), re_xyz[:,2])
            #     Rs.append(R)
            # Rs = torch.FloatTensor(Rs)
            # with torch.no_grad():
            #     A.data=Rs[:,0]
            #     B.data=Rs[:,1]
            #     D.data=Rs[:,2]
        G = [torch.FloatTensor(g) for g in G]
        # init generater
        # prov = batch_provider(G, 100)
        # da = prov.get()
        while i < 50 and res > res_th:
            # get minibatch
            # G_b = next(da)
            # G_b = [torch.FloatTensor(g) for g in G_b]
            i += 1
            # c0 = torch.FloatTensor([(c[0] - u[i][0]) / v[i][0] for i in range(num_planes)])
            # c1 = torch.FloatTensor([(c[1] - u[i][1]) / v[i][1] for i in range(num_planes)])
            # D = 1 - c0 * A - c1 * B
            loss = RLS(G, A, B, D)
            res = sum(loss) / N
            res.backward(retain_graph=True)
            for d in [A, B, D]:
                update(d, lr)
        with torch.no_grad():
            A1 = torch.zeros(num_planes)
            B1 = torch.zeros(num_planes)
            D1 = torch.zeros(num_planes)
            # de normalize
            for i in range(len(G)):
                D1[i] = D[i] * v[i][2] + u[i][2] - A[i] / v[i][0] * v[i][2] * u[i][0] - \
                       B[i] / v[i][1] * v[i][2] * u[i][1]
                A1[i] = A[i] / v[i][0] * v[i][2]
                B1[i] = B[i] / v[i][1] * v[i][2]
                G[i] = G[i].data.numpy() * v[i] + u[i]
            if vis:
                imo = scores.copy()
                # fig=plt.figure()
                ax0 = plt.axes()
                ax0.imshow(imo)
                ax0.scatter(c[0], c[1])
                # fig = plt.figure()
                # ax = Axes3D(fig)
            nplane = []
            for i in range(len(G)):
                x, y = intersec_point(A1[i - 1], B1[i - 1], D1[i - 1], A1[i], B1[i], D1[i])
                nplane.append([x, y])
                # imo[int(x), int(y)] = 2
                if vis:
                    ax0.scatter(x, y,c='r',alpha=itera/10)
                    # draw a 3D map
                    # ax.plot3D([box[i, 0], c[0]], [box[i, 1], c[1]], zs=[0, 1], color='r')
                    # ax.plot3D([x, c[0]], [y, c[1]], zs=[0, 1])
                    # z = A1[i].data.numpy() * G[i][:, 0] + B1[i].data.numpy() * G[i][:, 1] + D1[i].data.numpy()
                    # ax.plot_trisurf(G[i][:, 0], G[i][:, 1], z)
                    # ax.scatter3D(G[i][:, 0], G[i][:, 1], G[i][:, 2])
            nplane = np.array(nplane)
            planes = np.hstack([nplane, np.vstack([nplane[1:], nplane[0]])])
    if vis:
        plt.show()

def intersec_point(A1, B1, C1, A2, B2, C2):
    # z / gm[2] = ax / gm[0] + by / gm[1] + c
    m = A1 * B2 - A2 * B1
    if m == 0:
        print("无交点")
    else:
        x = (C2 * B1 - C1 * B2) / m
        y = (C1 * A2 - C2 * A1) / m
    return int(x), int(y)


def update(var, lr):
    var.data = var.data - var.grad.data * lr
    var.grad.zero_()
    return var


def near_plane(P, c, planes):
    # planes[4]:[{A: 0, B: -1/5, D: 0}, {A: 1/5, B: 0, D: -2}, {A: 0, B: 1/5, D: -2}, {A: -1/5, B: 0, D: 0}]
    G = [[] for i in range(len(planes))]
    vplanes = []
    for idx, plane in enumerate(planes):
        LM = np.hstack([plane, c])
        LM = LM.reshape(-1, 2)
        LM = np.hstack([LM, np.array([[1], [1], [1]])])
        vplanes.append(np.dot(np.linalg.inv(LM), np.array([0, 0, 1])))
    min_dist=np.array([10000]*P.shape[0],dtype=np.float32)
    ind=np.array([-1]*P.shape[0])
    for idx, plane in enumerate(vplanes):
        a = plane[0]
        b = plane[1]
        d = plane[2]
        dist = abs(a * P[:, 0] + b * P[:, 1] - P[:, 2] + d) / np.sqrt(a * a + b * b + 1)
        ind[dist < min_dist] = idx
        min_dist[dist < min_dist] = dist[dist < min_dist]
    for i in range(len(G)):
        G[i]=P[ind==i]
    return G, vplanes


def RLS(G, A, B, D):
    # Ax+By+D=z
    # loss = |z-Ax-By-D|
    losses = []
    for g, a, b, d in zip(G, A, B, D):
        loss = abs(g[:, 2] - a * g[:, 0] - b * g[:, 1] - d)
        losses.append(loss.sum())
    return losses

# def LSE(G):
#     # G :{0:[pi,p2,..],1:[],...}  p1=[x,y,z]
#     new_plane=[]
#     for idx,_ in enumerate(G):
#         points=G[idx]
#         a0 = Symbol('a0')
#         a1 = Symbol('a1')
#         a2 = Symbol('a2')
#         xi_squr=sum([i[0]*i[0] for i in points])
#         xi=sum([i[0] for i in points])
#         xi_yi=sum([i[0]*i[1] for i in points])
#         xi_zi = sum([i[0] * i[2] for i in points])
#         yi_squr = sum([i[1]*i[1] for i in points])
#         yi = sum([i[1] for i in points])
#         yi_zi=sum([i[1]*i[2] for i in points])
#         zi=sum([i[2] for i in points])
#         n=len(points)
#
#         tm=[]
#         tm.append(solve([a0 * xi_squr + a1 * xi_yi + a2 * xi - xi_zi, a0 * xi_yi + a1 * yi_squr + a2 *yi - yi_zi, a0 * xi + a1 * yi + a2*n - zi], [a0, a1, a2]))
#
#         # print(tm[0][a0],tm[0][a1],tm[0][a2])
#
#         A=tm[0][a0]*(-1)
#         B=tm[0][a1]*(-1)
#         D=tm[0][a2]*(-1)
#
#         new_plane.append([A,B,D])
#     return new_plane#,residual


if __name__ == "__main__":
    boxes = []
    box = np.array([[5., 1],
                    [35, 7],
                    [40, 19],
                    [1, 13]])
    boxes.append(box)
    i_h = 20
    i_w = 80
    im = np.zeros((i_h, i_w), dtype=np.uint8)
    init = cv2.fillPoly(im, [b.astype(np.int32) for b in boxes], 1)
    score = score_cal(i_h, i_w, boxes)
    # score = score_cal_old(i_h, i_w, boxes)
    score = random_noise(score, mode='gaussian', seed=None, var=(15/255.0)**2)
    # ####
    # import scipy.io as io
    # io.savemat('score.mat', {'score': score})
    # #####
    # start = time.time()
    plane_cluster(score)
    # print(time.time() - start)


    # tttttest(score[:, :30])
    # plt.imshow(init)
    # plt.show()
    # plt.imshow(score)
    # plt.show()
    # if IsInside(10, 30, 20, 0, 10, 30, 10, 15):
    # if IsInside(x1, y1, x2, y2, x3, y3, x, y):
    #     print
    #     "Inside"
    # else:
    #     print
    #     "Outside"
