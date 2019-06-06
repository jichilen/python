import os
import json
import numpy as np
import pycocotools.mask as mask_util
from tqdm import tqdm
import cv2
from shapely.geometry import *
from multiprocessing import Pool

def mask_iou(m1, m2):
    # m1, m2 binary mask
    inter = np.bitwise_and(m1, m2)
    union = np.bitwise_or(m1, m2)
    iou = np.sum(inter, None) / (np.sum(union, None) + 1e-6)
    return iou


def Mask_NMS(inds, scores, segs):
        '''

        :param inds: np.array (N, )
        :param scores:np.array (N, )
        :param segs: np.array(N, H, W)
        :return:
        '''
        score_thr = 0.3
        iou_thr = 0.2
        max_num = -1
        # threshold and sort
        thr = scores > score_thr
        inds, scores, segs = inds[thr], scores[thr], segs[thr]
        # areas = np.sum(segs.reshape(segs.shape[0], -1), -1)
        # sort = np.argsort(areas)[::-1]
        sort = np.argsort(scores)[::-1]
        inds, scores, segs = inds[sort], scores[sort], segs[sort]
        sup = np.ones(inds.shape, np.bool)
        # ious = np.zeros((len(inds), len(inds)))
        for i in range(len(inds)):
            if not sup[i]:
                continue
            for j in range(i + 1, len(inds)):
                # ious[i][j] = mask_iou(segs[i], segs[j])
                if sup[j]:
                    iou = mask_iou(segs[i], segs[j])
                    if iou > iou_thr:
                        sup[j] = False
        inds = inds[sup]
        if max_num != -1:
            min_num = min(max_num, len(scores[sup]))
            max_num_filter = np.argsort(-scores[sup])[:min_num]
            inds = inds[max_num_filter]
        return inds

def MASK(key,value):
    ind_list = []
    score_list = []
    seg_list = []
    for ind, score, seg in value:
        ind_list.append(ind)
        score_list.append(score)
        seg = mask_util.decode(seg)
        seg = cv2.resize(seg,(300,300))
        # TODO: add poly nms here
        seg_list.append(seg)
    inds = Mask_NMS(np.array(ind_list), np.array(score_list), np.array(seg_list))
    return inds

def POLY(key,value):
    ind_list = []
    score_list = []
    seg_list = []
    for ind, score, seg in value:
        ind_list.append(ind)
        score_list.append(score)
        seg = mask_util.decode(seg)
        # TODO: add poly nms here
        mask = np.array(seg[:, :, None], dtype=np.uint8)
        if cv2.__version__.startswith('4'):
            contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        elif cv2.__version__.startswith('3'):
            _, contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cons = []
        if contours:
            for co in contours[0]:
                cons.append(co[0])
            cons = np.array(cons)
            maskrect = cv2.minAreaRect(cons)
            box = cv2.boxPoints(maskrect)

        seg_list.append(box)
    inds = polygon_nms(np.array(ind_list), np.array(score_list), np.array(seg_list))
    return inds

def polygon_nms(inds,scores,polys):
    score_thr=0.3
    iou_thr=0.3
    max_num=1000
    thr = scores > score_thr
    inds, scores, polys = inds[thr], scores[thr], polys[thr]
    # areas = np.sum(segs.reshape(segs.shape[0], -1), -1)
    # sort = np.argsort(areas)[::-1]
    sort = np.argsort(scores)[::-1]
    inds, scores, polys = inds[sort], scores[sort], polys[sort]
    sup = np.ones(inds.shape, np.bool)
    # ious = np.zeros((len(inds), len(inds)))
    for i in range(len(inds)):
        if not sup[i]:
            continue
        for j in range(i + 1, len(inds)):
            # ious[i][j] = mask_iou(segs[i], segs[j])
            if sup[j]:
                iou = poly_iou(polys[i], polys[j])
                if iou > iou_thr:
                    sup[j] = False
    inds = inds[sup]
    if max_num != -1:
        min_num = min(max_num, len(scores[sup]))
        max_num_filter = np.argsort(-scores[sup])[:min_num]
        inds = inds[max_num_filter]
    return inds

def poly_iou(poly1,poly2):
    poly1=Polygon(poly1)
    poly2=Polygon(poly2)
    inse=poly1.intersection(poly2).area
    return inse/max((poly1.area+poly2.area-inse),1e-6)


if __name__ == '__main__':

    rootdir = './'
    # rname = 'full_results.pkl.json'
    rname = 'tasp_mst_info_r50_fpn_1x_all.pkl.json'
    results = json.load(open(os.path.join(rootdir, rname)))  # [dict]

    # {'bbox': [],
    #  'category_id': 1,
    #  'image_id': 1024,
    #  'score': 0.997943103313446,
    #  'segmentation': {'counts': '***','size': [375, 500]}}
    # mask_nms = Mask_NMS(score_thr=0.3, iou_thr=0.1)
    dets_per_image = dict()  # {[(), ()], []}
    for ind, result in enumerate(results):
        image_id = result['image_id']
        if not image_id in dets_per_image.keys():
            dets_per_image[image_id] = []
        else:
            dets_per_image[image_id].append((ind, result['score'], result['segmentation']))

    save_inds = []
    save_results = []
    p = Pool(4)
    for key, value in tqdm(dets_per_image.items(), ascii=True):
        # inds=POLY(key,value)
        inds = p.apply_async(MASK, args=(key,value,))

        # inds = mask_nms(np.array(ind_list), np.array(score_list), np.array(seg_list))
        save_inds.extend(inds.get())
        # print(inds)

        # exit(0)
    p.close()
    p.join()

    for i in save_inds:
        save_results.append(results[i])
    print(len(save_results))

    fp = open('../nms_results.pkl.json', 'w')
    fp.write(json.dumps(save_results))
