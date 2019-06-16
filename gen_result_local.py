import os

# not recommended
print("doing rm first, rm -rf ./result/*, please check if it is a wrong file")
os.system("rm -rf ./result/*")
import numpy as np
import argparse
import json
import pycocotools.mask as mask_util
from skimage import measure
from tqdm import tqdm
from utils import voc_eval_polygon
import cv2
# import from parent_dir
import sys
from multiprocessing import Pool
import time

sys.path.insert(0, '../')
from configs.all_text_data.path import DATASETS

parser = argparse.ArgumentParser(description="test scripts for curve polygons")
parser.add_argument("--data_dir", "-d", type=str, required=True,
                         help="you may choose from 'ART_val' and 'ctw_test', \
                         you can see all options in configs/all_text_data/path")
parser.add_argument("--pkl_json", "-p", type=str, required=True,
                         help="relative path to your results json file")
args = parser.parse_args()
rootdir = './'  #
# rootdir = '../../model/ART_giou/inference/ART_val/'
# rootdir=args.data_dir
# rname = 'results.pkl.json'
rname = args.pkl_json
results = json.load(open(os.path.join(rootdir, rname)))
annopath = DATASETS[args.data_dir]["ann_file"]
# annopath = '/data2/cyd/ctw1500_test.json'  #
# annopath = '/data2/data/ART/art_val.json'
thresh = 0.
# {'category_id': 1,
#  'image_id': 1001,
#  'score': 0.9890751838684082,
#  'segmentation': {'counts': '******',
#   'size': [240, 180]}}

def revise_binary_mask(seg):
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    opened = cv2.morphologyEx(seg, cv2.MORPH_OPEN, kernel)
    ret, labels = cv2.connectedComponents(opened)
    CCs = []
    areas = []
    for ind in range(ret):
        mask = np.zeros(labels.shape[:2], dtype=np.uint8)
        mask[np.where(labels == ind)] = 1
        CC = opened * mask
        closed = cv2.morphologyEx(CC, cv2.MORPH_CLOSE, kernel)
        CCs.append(closed)
        areas.append(np.sum(closed, None))
    seg = CCs[np.argsort(areas)[-1]]
    seg[[0, -1], :] = 0
    seg[:, [0, -1]] = 0
    return seg


def prepare_one_ann(re):
    seg = re['segmentation']
    seg = mask_util.decode(seg)  # imw*imh
    seg = revise_binary_mask(seg)
    contours = measure.find_contours(seg, 0.5)  # list[(n*2)] return row column  y x
    if len(contours) != 0:
        contours = [measure.subdivide_polygon(contours[0], 2)]
    with open('result/' + str(re['image_id']) + '.txt', 'a') as f:
        for contour in contours:
            contour = contour[:, [1, 0]]
            line = list(contour.reshape(-1))
            line = [str(l) for l in line]
            line = ','.join(line)
            # f.write(line+'\n')
            f.write('{:.5f}'.format(re['score']) + ',' + line + '\n')  # the first item is score

if __name__ == '__main__':


    if True:
        cal = 0
        p = Pool(12)
        start=time.time()
        for re in tqdm(results, ascii=True):
            if re['score'] < thresh:
                continue
            # cal+=1
            # if cal>4:
            #   break
            # prepare_one_ann(re)
            p.apply_async(prepare_one_ann, args=(re,))

        # exit(0)
        p.close()
        p.join()
        print(time.time()-start)
        anno_path = 'result/'
        outputstr = 'result_out/text'
        # score_thresh_list=[0.2, 0.3, 0.4, 0.5, 0.6, 0.62, 0.65, 0.7, 0.75, 0.8, 0.9]
        score_thresh_list = [0.5]
        iscore = 0.5
        files = os.listdir(anno_path)
        files.sort()
        # for iscore in score_thresh_list:
        det_out_lines=[]
        # with open(outputstr + str(iscore) + '.txt', "w") as f1:
        for ix, filename in enumerate(files):
            # print(filename)
            imagename = filename[:-4]
            # print(imagename)

            with open(os.path.join(anno_path, filename), "r") as f:
                lines = f.readlines()

            for line in lines:
                box = line.strip().split(",")
                assert (len(box) % 2 == 1), 'mismatch xy'
                out_str = "{} {}".format(str(int(imagename[:])), box[0])
                for i in box[1:]:
                    out_str = out_str + ' ' + str(i)
                det_out_lines.append(out_str + '\n')
                    # f1.writelines(out_str + '\n')

    # detpath = 'result_out/{:s}.txt'

    # score_thresh_list = [0.5]
    for isocre in score_thresh_list:
        rec, prec, ap, scores = voc_eval_polygon(det_out_lines, annopath, 'text', ovthresh=0.5)

    file = './txt_pr.txt'
    _ = lambda x, y: 2 * x * y * 1.0 / (x + y)
    max_f = [0, 0, 0, 0, 0]
    with open(file, 'w') as f:
        f.write('ap     rec    prec   f-measure\n')
        for i in range(len(rec)):
            f_mean = _(rec[i], prec[i])
            if max_f[3] < f_mean:
                max_f = [ap, rec[i], prec[i], f_mean, i]
            f.write('{:.4f} {:.4f} {:.4f} {:.4f}\n'.format(ap, rec[i], prec[i], f_mean))
        print('ap: {:.4f}, recall: {:.4f}, pred: {:.4f}, FM: {:.4f}'.format(ap, rec[-1], prec[-1], _(rec[-1], prec[-1])))
        print("max f-measure threshold: {}".format(-scores[max_f[-1]]))
        print('ap: {:.4f}, recall: {:.4f}, pred: {:.4f}, FM: {:.4f}'.format(*max_f))
