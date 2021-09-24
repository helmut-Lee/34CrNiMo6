# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:17:45 2021

@author: helmut
"""
#8. make video from png images.vim

import numpy as np, cv2, glob, os

path2='D:/LTRANS/YECS_sarga_2020wnd1/output_apw_0/'
dlist2=os.listdir(path2)

for j in dlist2:    
    flist2=sorted(glob.glob(path2+j+'/figure/'+'*.png'))
    img_array=[]
    for i in flist2:    
        img=cv2.imread(i)
        height, width, layers=img.shape
        size=(width, height)
        img_array.append(img)
    
    video=cv2.VideoWriter(path2+j+'/figure/'+j[6:14]+'.mp4', cv2.VideoWriter_fourcc(*'DIVX'), fps=2.5, frameSize=size, isColor=True)
    for i in range(len(img_array)):
        video.write(img_array[i])
    video.release()