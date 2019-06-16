import struct
import numpy as np
import glob
import cv2
import json
filenames=glob.glob('*.dgr')
for filename in filenames:
    fp=open(filename,'rb')
    #
    # x pad byte    no value
    # c char    bytes of length 1   1
    # b signed char integer 1
    # B unsigned char   integer 1
    # ? _Bool   bool    1
    # h short   integer 2
    # H unsigned short  integer 2
    # i int integer 4
    # I unsigned int    integer 4
    # l long    integer 4
    # L unsigned long   integer 4
    # q long long   integer 8
    # Q unsigned long long  integer 8
    # n ssize_t integer
    # N size_t  integer
    # e     float   2
    # f float   float   4
    # d double  float   8
    # s char[]  bytes
    data=fp.read(4)
    iHdSize=struct.unpack('i',data)[0]
    data=fp.read(8)
    szFormatCode=struct.unpack('8s',data)[0]
    data=fp.read(iHdSize - 36)
    szIllustr=struct.unpack('{}s'.format(iHdSize - 36),data)[0]
    data=fp.read(20)
    szCodeType=struct.unpack('20s',data)[0]
    data=fp.read(2)
    sCodeLen=struct.unpack('h',data)[0]
    data=fp.read(2)
    sBitApp=struct.unpack('h',data)[0]
    data=fp.read(4)
    iImgHei=struct.unpack('i',data)[0]
    data=fp.read(4)
    iImgWid=struct.unpack('i',data)[0]
    data=fp.read(4)
    iLineNum=struct.unpack('i',data)[0]
    img=np.ones((iImgHei,iImgWid),dtype=np.uint8)*255
    jsonname=filename[:-3]+'json'
    imname = filename[:-3] + 'jpg'
    labels=[]
    charbboxs=[]
    for i in range(iLineNum):
        data=fp.read(4)
        iWordNum=struct.unpack('i',data)[0]
        la=[]
        charbox=[]
        for j in range(iWordNum):
            data=fp.read(sCodeLen)
            pWordLabel=data.decode('gbk').replace('\x00','')
            data=fp.read(2*4)
            sTop,sLeft,sHei,sWid=struct.unpack('h'*4,data)
            data=fp.read(sHei*sWid)
            pTmpData=struct.unpack('B'*sHei*sWid,data)
            pTmpData=np.array(pTmpData).reshape(sHei,sWid)
            img[sTop:sTop+sHei,sLeft:sLeft+sWid]=pTmpData
            charbox.append([sLeft,sTop,sWid,sHei])
            la.append(pWordLabel)
        labels.append(la)
        charbboxs.append(charbox)
    cv2.imwrite(imname,img)
    json.dump({'labels':labels,'charbboxs':charbboxs},open(jsonname,'w'),indent=4)
ppp=1