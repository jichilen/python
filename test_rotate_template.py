import cv2
from matplotlib import pyplot as plt
import numpy as np


def get_larger_box(curBox, W, H, beta):
    # let's make the region of search larger for the current box.
    if beta == 0: return curBox
    left, top, right, bottom = curBox
    centerX = (left + right) / 2
    centerY = (top + bottom) / 2
    width = right - left + 1
    height = bottom - top + 1

    largerBox = np.zeros(4)
    largerBox[0], largerBox[2] = centerX - (width / 2 + beta), centerX + (width / 2 + beta)
    largerBox[1], largerBox[3] = centerY - (height / 2 + beta), centerY + (height / 2 + beta)
    return largerBox


if __name__ == '__main__':
    beta = 200
    im = cv2.imread(r"D:\data\service\Newport\tsvis\tr_img_00001.jpg")

    h, w = im.shape[:2]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    # 第三个参数：变换后的图像大小
    res = cv2.warpAffine(im, M, (w, h))
    M = cv2.getRotationMatrix2D((w / 2, h / 2), 5, 1)
    # 第三个参数：变换后的图像大小
    im1 = cv2.warpAffine(im, M, (w, h))
    im2 = cv2.copyMakeBorder(im1, beta, beta, beta, beta, cv2.BORDER_REPLICATE)
    # 66 648 544 873
    last_track = [66, 648, 544, 873]
    cv2.rectangle(im, (int(last_track[0]), int(last_track[1])), (int(last_track[2]), int(last_track[3])), (255, 0, 0),
                  4)
    plt.imshow(im)
    plt.show()
    lastWidth, lastHeight = last_track[2] - last_track[0] + 1, last_track[3] - last_track[1] + 1
    lastBoxImage = im[int(last_track[1]):int(last_track[3] + 1),
                   int(last_track[0]):int(last_track[2] + 1)]
    searchRegion = list(map(int, get_larger_box(last_track[:4], w, h, beta)))
    searchRegion = [sea_ind+beta for sea_ind in searchRegion]
    searchRegionImage = im2[searchRegion[1]:searchRegion[3] + 1,
                        searchRegion[0]:searchRegion[2] + 1]
    matchResult = cv2.matchTemplate(searchRegionImage, lastBoxImage, cv2.TM_CCOEFF_NORMED)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(matchResult)
    topLeft = maxLoc
    bottomRight = (topLeft[0] + lastWidth, topLeft[1] + lastHeight)
    trackedBox = [searchRegion[0] + topLeft[0], searchRegion[1] + topLeft[1],
                  searchRegion[0] + bottomRight[0], searchRegion[1] + bottomRight[1], 0, 0, 0]
    trackedBox[0] = max(0, trackedBox[0] - beta)
    trackedBox[1] = max(0, trackedBox[1] - beta)
    trackedBox[2] = min(trackedBox[2] - beta, w - 1)
    trackedBox[3] = min(trackedBox[3] - beta, h - 1)

    cv2.rectangle(im1, (int(trackedBox[0]), int(trackedBox[1])), (int(trackedBox[2]), int(trackedBox[3])), (255,0,0), 4)
    plt.imshow(im1)
    plt.show()
#     im1 = np.zeros(im.shape).astype(im.dtype)
#     h,w = im.shape[:2]
#     im1[:,0:w-50,:] = im[:,50:,:]
#     # TODO :check matchTemplate
#     #   move left and whether is can be matched
#     #   move right and check whether it can be matched
#     im2=cv2.copyMakeBorder(im1, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
#     # im2=np.zeros(im1.shape+np.array([200,200,0])).astype(im.dtype)
#     # im2[100:-100,100:-100] = im1
#     last_track = [0,200,200,300]
#     lastWidth, lastHeight = last_track[2] - last_track[0] + 1, last_track[3] - last_track[1] + 1
#     lastBoxImage = im[int(last_track[1]):int(last_track[3] + 1),
#                    int(last_track[0]):int(last_track[2] + 1)]
#     searchRegion = list(map(int, get_larger_box(last_track[:4], w, h, 100)))
#     searchRegion = [sea_ind+100 for sea_ind in searchRegion]
#     searchRegionImage = im2[searchRegion[1]:searchRegion[3] + 1,
#                         searchRegion[0]:searchRegion[2] + 1]
#     matchResult = cv2.matchTemplate(searchRegionImage, lastBoxImage, cv2.TM_CCOEFF_NORMED)
#     (_, maxVal, _, maxLoc) = cv2.minMaxLoc(matchResult)
#     topLeft = maxLoc
#     bottomRight = (topLeft[0] + lastWidth, topLeft[1] + lastHeight)
#     trackedBox = [searchRegion[0] + topLeft[0], searchRegion[1] + topLeft[1],
#                   searchRegion[0] + bottomRight[0], searchRegion[1] + bottomRight[1], 0, 0, 0]
#     trackedBox[0] = max(0, trackedBox[0] - 100)
#     trackedBox[1] = max(0, trackedBox[1] - 100)
#     trackedBox[2] = min(trackedBox[2] - 100, w - 1)
#     trackedBox[3] = min(trackedBox[3] - 100, h - 1)
# 
#     cv2.rectangle(im1, (int(trackedBox[0]), int(trackedBox[1])), (int(trackedBox[2]), int(trackedBox[3])), (255,0,0), 4)
#     plt.imshow(im1)
#     plt.show()
#     plt.imshow(searchRegionImage)
#     plt.show()
#     plt.imshow(lastBoxImage)
#     plt.show()
#     plt.imshow(matchResult)
#     plt.show()
# ###### reverse
#     im1 = np.zeros(im.shape).astype(im.dtype)
#     im1[:, 0:w - 50, :] = im[:, 50:, :]
#     im = im[:,::-1,:]
#     im1 = im1[:,::-1,:]
#     im1 = im1.copy()
#     plt.imshow(im)
#     plt.show()
#     last_track = [w-100, 200, w, 300]
#     im2=cv2.copyMakeBorder(im1, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
#     # im2 = np.zeros(im1.shape + np.array([200, 200, 0])).astype(im.dtype)
#     # im2[100:-100, 100:-100] = im1
#     im1 = im2.copy()
#     lastWidth, lastHeight = last_track[2] - last_track[0] + 1, last_track[3] - last_track[1] + 1
#     lastBoxImage = im[int(last_track[1]):int(last_track[3] + 1),
#                    int(last_track[0]):int(last_track[2] + 1)]
#     searchRegion = list(map(int, get_larger_box(last_track[:4], w, h, 100)))
#     searchRegion = [sea_ind + 100 for sea_ind in searchRegion]
#     searchRegionImage = im1[searchRegion[1]:searchRegion[3] + 1,
#                         searchRegion[0]:searchRegion[2] + 1]
#     matchResult = cv2.matchTemplate(searchRegionImage, lastBoxImage, cv2.TM_CCOEFF_NORMED)
#     (_, maxVal, _, maxLoc) = cv2.minMaxLoc(matchResult)
#     topLeft = maxLoc
#     bottomRight = (topLeft[0] + lastWidth, topLeft[1] + lastHeight)
#     trackedBox = [searchRegion[0] + topLeft[0], searchRegion[1] + topLeft[1],
#                   searchRegion[0] + bottomRight[0], searchRegion[1] + bottomRight[1], 0, 0, 0]
#     cv2.rectangle(im1, (int(trackedBox[0]), int(trackedBox[1])), (int(trackedBox[2]), int(trackedBox[3])), (255, 0, 0),
#                   4)
#     plt.imshow(im1)
#     plt.show()
#     plt.imshow(searchRegionImage)
#     plt.show()
#     plt.imshow(lastBoxImage)
#     plt.show()
#     plt.imshow(matchResult)
#     plt.show()
#     ppp=1
