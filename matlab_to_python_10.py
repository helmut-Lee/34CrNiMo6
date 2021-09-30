#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:56:10 2021

@author: Helmut.J.Lee
"""
#10. LTRANS.csv plotting.

import numpy as np, pandas as pd, matplotlib.pyplot as plt, netCDF4 as nc, glob, os
from mpl_toolkits.basemap import Basemap

# os.chdir('E:/remembernokorean/python/')
path='D:/LTRANS/YECS_sarga_2020wnd1/output_apw_b1/'
path2='D:/LTRANS/YECS_sarga_2020wnd1/output_apw_b0/'
path3='D:/output2016-2019/'
dlist, dlist2=os.listdir(path), os.listdir(path2)
# os.mkdir(path2+dlist2[0]+'/figure')
flist=sorted(glob.glob(path+dlist[0]+'/*.csv'))
flist2=sorted(glob.glob(path2+dlist2[0]+'/*.csv'))

# A=pd.date_range('2019-04-01 12:00', periods=120, freq='+1d').strftime('%Y-%m-%d %H:%M') # fwd
A=pd.date_range('2019-04-01 12:00', periods=180, freq='-1d').strftime('%Y-%m-%d %H:%M') # bwd

for i in range(round(len(flist)/24)):
    C=pd.read_csv(flist[(i*24)+1], header=None, index_col=False)
    D=pd.read_csv(flist2[(i*24)+1], header=None, index_col=False)
    C, D=np.array(C), np.array(D)
    
    if flist[1][50:58]=='20170213':
        j=410
    elif flist[1][50:58]=='20170413':
        j=469
    elif flist[1][50:58]=='20170429':
        j=485
    elif flist[1][50:58]=='20170518':
        j=504
    elif flist[1][50:58]=='20170602':
        j=519
    elif flist[1][50:58]=='20180328':
        j=818
    elif flist[1][50:58]=='20180420':
        j=841
    elif flist[1][50:58]=='20180504':
        j=855
    elif flist[1][50:58]=='20190313':
        j=1168
    elif flist[1][50:58]=='20190401':
        j=1187
    else:
        j=1219 # '20190503'
    
    # B=nc.Dataset(path3+'yecs15_his_'+f'{j+i:04d}.nc', 'r', format='NETCDF4') # fwd
    B=nc.Dataset(path3+'yecs15_his_'+f'{j-i:04d}.nc', 'r', format='NETCDF4') # bwd
    mask=B['mask_rho'][::8, ::8]    
    angle=B['angle'][::8, ::8]
    uwind=B['Uwind'][2, ::8, ::8] # 12:00 KST
    vwind=B['Vwind'][2, ::8, ::8]
    mask=np.where(mask==0, np.nan, mask)    
    uvlon, uvlat=B['lon_rho'][::8, ::8], B['lat_rho'][::8, ::8]
    
    u3d1=uwind*np.cos(angle)-vwind*np.sin(angle)
    v3d1=uwind*np.cos(angle)+vwind*np.sin(angle)
    u3d1, v3d1=np.where(u3d1>100, np.nan, u3d1), np.where(v3d1>100, np.nan, v3d1)    
        
    # plt.rcParams['font.family']='malgun gothic'
    plt.rcParams['font.family']='tahoma'    
    plt.figure(figsize=(10, 13), dpi=75)
    M=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')    
    M.drawcoastlines(color='#000000')
    M.drawmapboundary(color='#000000', linewidth=2)
    M.fillcontinents(color='#000000')
    M.drawparallels(np.arange(26, 41, 2), labels=[1, 0, 0, 0], size=22)
    M.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=22)    
    xt, yt=M(C[:,2], C[:,3])
    xt2, yt2=M(D[:,2], D[:,3])
    xt3, yt3=M(uvlon, uvlat)
    q = M.quiver(xt3, yt3, u3d1, v3d1, scale=120, headwidth=5, headaxislength=10,
                  headlength=13, color='#555555', minlength=1, edgecolor='y', minshaft=1.3, alpha=.7)    
    apw1=M.scatter(xt, yt, c='#FF0000', s=1)
    apw0=M.scatter(xt2, yt2, c='#0000FF', s=1)
    plt.legend([apw1, apw0], ['apw = 1', 'apw = 0'], fontsize=22, markerscale=22, loc=1)
    plt.title(A[i]+' KST (start : 2019-04-01)', fontsize=30)
    plt.tight_layout() # reduce white space layout.
    plt.savefig(path2+dlist2[0]+'/figure/'+flist[(i*24)+1][63:75]+'.png',format='png',
                facecolor=None, edgecolor=None, transparent=True)
    plt.show()
    
# ======================================================================
# black background figure
# plt.rcParams['font.family']='tahoma'    
# plt.rcParams['axes.facecolor']='#000000'
# plt.rcParams['text.color']='#FFFFFF'
# plt.figure(facecolor='#000000',figsize=(10, 13), dpi=75)
# M=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')    
# M.drawcoastlines(color='#FFFFFF')
# M.drawmapboundary(color='#FFFFFF', fill_color='#000000', linewidth=2)
# M.fillcontinents(color='#FFFFFF', lake_color='#000000')
# M.drawparallels(np.arange(26, 41, 2), labels=[1, 0, 0, 0], size=22, color='#FFFFFF', textcolor='#FFFFFF')
# M.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=22, color='#FFFFFF', textcolor='#FFFFFF')
# xt, yt=M(C[:,2], C[:,3])
# xt2, yt2=M(D[:,2], D[:,3])
# xt3, yt3=M(uvlon, uvlat)
# q = M.quiver(xt3, yt3, u3d1, v3d1, scale=120, headwidth=5, headaxislength=10,
#               headlength=13, color='#BBBBBB', minlength=1, edgecolor='y', minshaft=1.3, alpha=.7)
# plt.axis('equal')
# Unit vector
# p = plt.quiverkey(q, M(118), M(40), 1, "1 m/s",coordinates='data',color='r', labelpos='S', alpha=1, 
#                   labelcolor='w', fontproperties={'size':16}, labelsep=0.13)    
# apw1=M.scatter(xt, yt, c='#FF0000', s=1)
# apw0=M.scatter(xt2, yt2, c='#0000FF', s=1)
# plt.legend([apw1, apw0], ['apw = 1', 'apw = 0'], fontsize=22, markerscale=22, loc=1)
# plt.title(A[i]+' KST (start : 2019-04-01)', fontsize=30)
# plt.tight_layout() # reduce white space layout.
# plt.show()
# ======================================================================
# print(f'{2:01d}')
# print(f'{2:02d}')
# print(f'{2:03d}')
# print(f'{2:04d}')

# print(f'{2.7:0.1f}')
# print(f'{2.7:0.2f}')
# print(f'{2.7:0.3f}')
# print(f'{2.7:0.4f}')
