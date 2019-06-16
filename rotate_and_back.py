import cv2
import numpy as np
import matplotlib.pyplot as plt
# from mmdet.core.post_processing.bbox_nms import multiclass_nms
def vis(im, box, seg, labels):
    im_o = im.copy()
    seg = np.array(seg).reshape((-1, 2)).astype(np.int32)
    print(seg)
    # cv2.rectangle(im_o, (box[0], box[1]), (box[2], box[3]), (255, 0, 0), 2)
    cv2.polylines(im_o, [seg], True, (0, 0, 255), 2)
    # cv2.namedWindow('1',cv2.WINDOW_NORMAL)
    # cv2.imshow('1',im_o)
    # cv2.waitKey()
    plt.imshow(im_o)
    plt.show()

img=cv2.imread('D:\data\ReCTs\img/train_ReCTS_000001.jpg')
segment=np.array([25, 175, 112, 175, 112, 286, 25, 286]).reshape(-1,2)
vis(img,None,segment,None)
mode=-30
(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)
# grab the rotation matrix (applying the negative of the
# angle to rotate clockwise), then grab the sine and cosine
# (i.e., the rotation components of the matrix)
M = cv2.getRotationMatrix2D((cX, cY), -mode, 1.0)
cos = np.abs(M[0, 0])
sin = np.abs(M[0, 1])
# compute the new bounding dimensions of the image
nW = int((h * sin) + (w * cos))
nH = int((h * cos) + (w * sin))
# adjust the rotation matrix to take into account translation
M[0, 2] += (nW / 2) - cX
M[1, 2] += (nH / 2) - cY
# perform the actual rotation and return the image
img1 = cv2.warpAffine(img, M, (nW, nH))
# when we have the sin cos of the trans, we can cal the segs
out_segments = []
boxes = []
mode = np.pi / 180 * mode
(h, w) = img1.shape[:2]
(cX_n, cY_n) = (w // 2, h // 2)

segment = np.array(segment).reshape(-1, 2) - np.array([cX, cY])
out_seg = segment.copy()
out_seg[:, 0] = np.cos(mode) * segment[:, 0] - np.sin(mode) * segment[:, 1]
out_seg[:, 1] = np.cos(mode) * segment[:, 1] + np.sin(mode) * segment[:, 0]
out_seg += np.array([cX_n, cY_n])
x1, y1 = np.min(out_seg, 0)
x2, y2 = np.max(out_seg, 0)
vis(img1,None,out_seg,None)

mode=-mode
segment = out_seg
segment = np.array(segment).reshape(-1, 2) - np.array([cX_n, cY_n])
out_seg = segment.copy()
out_seg[:, 0] = np.cos(mode) * segment[:, 0] - np.sin(mode) * segment[:, 1]
out_seg[:, 1] = np.cos(mode) * segment[:, 1] + np.sin(mode) * segment[:, 0]
out_seg += np.array([cX, cY])
vis(img,None,out_seg,None)