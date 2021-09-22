#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:56:10 2021

@author: Helmut.J.Lee
"""
#10. LTRANS.csv plotting.

import numpy as np, pandas as pd, matplotlib.pyplot as plt, netCDF4 as nc, glob, os
from mpl_toolkits.basemap import Basemap

os.chdir('E:/remembernokorean/python/')
# path='D:/LTRANS/YECS_sarga_2020wnd1/output20170518/' # ocnp
# path2='D:/LTRANS/YECS_sarga_2020wnd1/output20170518_apw0/' # ocnp
path='D:/LTRANS/YECS_sarga_2020wnd1/output20170413/' # ocnp
path2='D:/LTRANS/YECS_sarga_2020wnd1/output20170413_apw0/' # ocnp
path3='D:/output2017/' # ocnp
# path='C:/Users/262mi/Documents/output/' # Windows
# path='/home/helmut/USB/remembernokorean/python/output_0413/' # Linux
# path2, path3=path, path # dormitory
# os.mkdir(path2+'figure')

flist=sorted(glob.glob(path+'*.csv'))
flist2=sorted(glob.glob(path2+'*.csv'))

A=pd.date_range('2017-04-13 12:00', periods=120, freq='+1d').strftime('%Y-%m-%d %H:%M')

for i in range(round(len(flist)/24)):
    C=pd.read_csv(flist[(i*24)+1], header=None, index_col=False) # ocnp
    # D=pd.read_csv(flist2[(i*24)+1], header=None, index_col=False) # ocnp
    D=pd.read_csv(flist[(i*24)], header=None, index_col=False) # dormitory
    C, D=np.array(C), np.array(D)

    B=nc.Dataset(path3+'yecs15_his_'+f'{i+548:04d}.nc', 'r', format='NETCDF4') # 469
    mask=B['mask_rho'][::8, ::8]    
    angle=B['angle'][::8, ::8]
    uwind=B['Uwind'][2, ::8, ::8] # 12:00 KST
    vwind=B['Vwind'][2, ::8, ::8]
    mask=np.where(mask==0, np.nan, mask)
    
    uvlon, uvlat=B['lon_rho'][::8, ::8], B['lat_rho'][::8, ::8]
    
    u3d1=uwind*np.cos(angle)-vwind*np.sin(angle)
    v3d1=uwind*np.cos(angle)+vwind*np.sin(angle)
    u3d1, v3d1=np.where(u3d1>100, np.nan, u3d1), np.where(v3d1>100, np.nan, v3d1)
    
    
    plt.figure(figsize=(15, 19.5), dpi=100)
    M=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')
    M.drawcoastlines(color='#000000')
    M.drawmapboundary(color='#000000', linewidth=2)
    M.fillcontinents(color='#000000')
    M.drawparallels(np.arange(26, 41, 2), labels=[1, 0, 0, 0], size=28)
    M.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=28)
    xt, yt=M(C[:,2], C[:,3])
    xt2, yt2=M(D[:,2], D[:,3])
    xt3, yt3=M(uvlon, uvlat)
    q = M.quiver(xt3, yt3, u3d1, v3d1, scale=120, headwidth=5, headaxislength=10,
                  headlength=13, color='#666666', minlength=1, edgecolor='y', minshaft=1.3, alpha=.7)
    # plt.axis('equal')
    # Unit vector
    # p = plt.quiverkey(q, M(118), M(40), 1, "1 m/s",coordinates='data',color='r', labelpos='S', alpha=1, 
    #                   labelcolor='w', fontproperties={'size':16}, labelsep=0.13)    
    # M.scatter(xt, yt, c='#B7BD04', s=4)
    apw1=M.scatter(xt, yt, c='#FF0000', s=1)
    apw0=M.scatter(xt2, yt2, c='#0000FF', s=1)
    plt.legend([apw1, apw0], ['apw = 1', 'apw = 0'], fontsize=32, markerscale=32, loc=1)
    plt.title(A[i+79]+' KST (start : 2017-04-13)', fontsize=40) # 79
    # plt.savefig(path2+'figure/'+flist[(i*24)+1][45:57]+'.png',format='png',
    #             facecolor=None, edgecolor=None, transparent=True)
    # plt.savefig('C:/Users/helmut/Desktop/transparent_test.png',format='png',
    #             facecolor=None, edgecolor=None, transparent=True)
    plt.show()
    
# ======================================================================
# print(f'{2:01d}')
# print(f'{2:02d}')
# print(f'{2:03d}')
# print(f'{2:04d}')

# print(f'{2.7:0.1f}')
# print(f'{2.7:0.2f}')
# print(f'{2.7:0.3f}')
# print(f'{2.7:0.4f}')