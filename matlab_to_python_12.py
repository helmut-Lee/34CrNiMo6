#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:56:10 2021

@author: Helmut.J.Lee
"""
#12. read coordinate.csv and append

import numpy as np, pandas as pd, matplotlib.pyplot as plt, glob
from mpl_toolkits.basemap import Basemap

path='/home/helmut/python/S.Horneri/GOCI_project/location13/'
total='/home/helmut/python/S.Horneri/GOCI_project/total_csv/'

box_list=sorted(glob.glob(path+'box*.csv'))
# NDVI_list=sorted(glob.glob(path+'NDVI*.csv')) # if you use manual mode, this will be disabled.

for i in range(len(box_list)):
    globals()['a{}'.format(i)]=pd.DataFrame()
    box=pd.read_csv(box_list[i], header=None, index_col=False, names=[0, 1, 2, 3])
    box.drop(columns=[2, 3], axis=1, inplace=True)
    box[2], box[3]=0, 0
    
    # ndvi=pd.read_csv(NDVI_list[i], header=0, index_col=False, names=[4, 0, 1])    
    # ndvi.drop(columns=4, axis=1, inplace=True)
    # ndvi[2], ndvi[3]=0, 0
    
    # globals()['a{}'.format(i)]=box.append(ndvi, ignore_index=True) # semiauto
    globals()['a{}'.format(i)]=box # manual
    
total_csv=a0.append([a1, a2], ignore_index=True)
total_csv.drop_duplicates(inplace=True)
total_csv=np.array(total_csv)

# jeju=np.where((total_csv[:,1]>33.1) & (total_csv[:,1]<33.6) & (total_csv[:,0]>126.1) & (total_csv[:,0]<127))
# cloud=np.where((total_csv[:,1]>30.9) & (total_csv[:,1]<31.1) & (total_csv[:,0]>125) & (total_csv[:,0]<125.4))
# total_csv=np.delete(total_csv, jeju, axis=0)

plt.figure(figsize=(10, 13), dpi=75)
N=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')
N.drawcoastlines()
N.drawmapboundary(color='#000000', linewidth=2)
N.fillcontinents(color='#000000')
N.drawparallels(np.arange(25, 41, 2), labels=[1, 0, 0, 0], size=22)
N.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=22)
xt, yt=N(total_csv[:,0], total_csv[:,1])
N.scatter(xt, yt, c='#B46404', s=1)
plt.title('2017-05-07', fontsize=30)
plt.show()

total_csv=pd.DataFrame(total_csv)
total_csv.to_csv(total+'box_total_20170507031641.csv')


