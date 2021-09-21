#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:20:58 2020

@author: Helmut.J.Lee
"""
import os
import numpy as np
import pandas as pd
import time

t=time.time()
path='D:/remembernokorean/python/report/' ## Windows
#path='/home/helmut/USB/remembernokorean/python/report/' ## Linux
flist=sorted(os.listdir(path))
col=np.arange(503,250,-3)
result=pd.DataFrame(index=range(0,len(flist)),
                    columns=['file name','B peak','T peak','A peak',
                             'M peak','C peak','D peak','E peak','N peak'])
for i in range(len(flist)):
    data=pd.read_csv(path+flist[i],sep='\t',header=1,names=col)
    data.iloc[0,0:]=col
    result.iloc[i,0]=flist[i] # each file name
    result.iloc[i,1]=data.iloc[16,np.where(data.iloc[0,:]==275)[0][0]] # B_peak
    result.iloc[i,2]=data.iloc[23,np.where(data.iloc[0,:]==275)[0][0]] # T_peak
    result.iloc[i,3]=max(data.iloc[34:48,np.where(data.iloc[0,:]==260)[0]].max()) # A_peak
    result.iloc[i,4]=max(data.iloc[28:37,np.where((data.iloc[0,:]>=290) & (data.iloc[0,:]<=310))[0]].max()) # M_peak
    result.iloc[i,5]=max(data.iloc[39:48,np.where((data.iloc[0,:]>=320) & (data.iloc[0,:]<=360))[0]].max()) # C_peak
    result.iloc[i,6]=data.iloc[58,np.where(data.iloc[0,:]==389)[0][0]] # D_peak
    result.iloc[i,7]=data.iloc[60,np.where(data.iloc[0,:]==455)[0][0]] # E_peak
    result.iloc[i,8]=data.iloc[28,np.where(data.iloc[0,:]==281)[0][0]] # N_peak

elapsed=time.time()-t
print('elapsed time is '+str(elapsed)+'sec.')

#result.to_excel('/home/helmut/.config/spyder-py3/FDOM_result.xlsx') # Linux
result.to_excel('D:/remembernokorean/python/report/FDOM_result.xlsx') # Windows


#used system
#cpu : intel i3-4150
#ram : 8GB
#OS  : kubuntu 20.04.1
#cal.program : python 3.8.5