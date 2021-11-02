#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 13:56:33 2021

@author: Helmut.J.Lee
"""
#6. 2-dimension data interpolation(griddata)

import numpy as np, pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
from scipy.interpolate import griddata

path='F:/remembernokorean/matlab/' # Windows
# path='/home/helmut/USB/remembernokorean/matlab/' # Linux

lon=np.array([126.2, 126.2, 126.2,
     126, 126, 126, 126, 126, 126,
     125.8, 125.8, 125.8, 125.8, 125.8, 125.8,
     125.6, 125.6, 125.6, 125.6, 125.6, 125.6])
lat=np.array([33.5, 33.6, 33.7,
     33.2, 33.3, 33.4, 33.5, 33.6, 33.7, 
     33.2, 33.3, 33.4, 33.5, 33.6, 33.7, 
     33.2, 33.3, 33.4, 33.5, 33.6, 33.7])

col_name=np.arange(0, 8)
t=np.full([21],np.nan)

for i in range(21):
    data=pd.read_csv(path+f'St{i+1:02d}.dat', sep='\s+', names=col_name, header=None, index_col=None)
    depth=data.iloc[:,1]
    t[i]=data.iloc[depth[depth==20].index[0],2] # find index in dataframe or series.
    
LON, LAT=np.meshgrid(np.arange(125.6, 126.2, 0.01), np.arange(33.2, 33.7, 0.01))
grid_1=griddata((lon, lat), t, (LON, LAT), method='cubic')

plt.figure(figsize=(12,8), dpi=200.0)
B=Basemap(projection='mill', llcrnrlat=33, urcrnrlat=34,
          llcrnrlon=125.3, urcrnrlon=126.8, resolution='h')
B.drawcoastlines()
B.drawmapboundary(color='#000000', linewidth=2)
B.fillcontinents(color='#e0e0e0')
xt, yt=B(lon, lat)
xt2, yt2=B(LON, LAT)
Bs=plt.contourf(xt2, yt2, grid_1, cmap='jet')
B.scatter(xt, yt, marker='.', edgecolors='#000000')
for i in range(21):
    plt.text(xt[i]+2000,yt[i]-1000,f'St.{i+1:02d}', fontsize=8)
plt.show()
