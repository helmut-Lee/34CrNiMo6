#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 14:56:10 2021

@author: Helmut.J.Lee
"""
#11. read sargassum.csv and plotting.

import numpy as np, pandas as pd, matplotlib.pyplot as plt, glob
from mpl_toolkits.basemap import Basemap

path='/home/pang/tmp/helmut/GOCI_project_supplement/location2/'
total='/home/pang/tmp/helmut/GOCI_project_supplement/total_csv/'
#===========CSV_red dot==============#

A=pd.read_csv(path+'box00_20170602031643.csv', header=None, index_col=False)
A.drop(columns=[2, 3], axis=1, inplace=True)
D=pd.read_csv(path+'box01_20170602031643.csv', header=None, index_col=False)
D.drop(columns=[2, 3], axis=1, inplace=True)

# B=pd.read_csv(total+'box_total_20170413031644.csv', names=[2, 0, 1], header=0, index_col=False)
B=pd.read_csv(total+'box_total_20170602031643.csv', names=[2, 0, 1], header=0, index_col=False)
# B.drop(columns=0, axis=1, inplace=True)
B.drop(columns=2, axis=1, inplace=True)

C=A.append([B, D], ignore_index=True)
C=np.array(C)
# box_4=C


# box_total=box_0.append([box_1, box_2, box_3, box_4], ignore_index=True)
# box_total=np.array(box_total)

# jeju=np.where((box_total[:,1]>33.1) & (box_total[:,1]<33.6) & (box_total[:,0]>126.1) & (box_total[:,0]<127))
# cloud=np.where((box_total[:,1]>30.9) & (box_total[:,1]<31.1) & (box_total[:,0]>125) & (box_total[:,0]<125.4))
# box_total=np.delete(box_total, jeju, axis=0)

plt.figure(figsize=(15, 19.5), dpi=100)
N=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=38, llcrnrlon=120, urcrnrlon=130, resolution='h')
N.drawcoastlines()
N.drawmapboundary(color='#000000', linewidth=2)
N.fillcontinents(color='#000000')
N.drawparallels(np.arange(25, 39, 2), labels=[1, 0, 0, 0], size=28)
N.drawmeridians(np.arange(120, 131, 2), labels=[0, 0, 0, 1], size=28)
# xt, yt=N(box_total[:,0], box_total[:,1])
xt, yt=N(C[:,0], C[:,1])
N.scatter(xt, yt, c='#FF0000', s=1)
plt.title('2017-06-02', fontsize=48)
plt.show()

# box_total=pd.DataFrame(box_total)
# box_total.to_csv(total+'box_total_20170429031643_supplemented.csv')
C=pd.DataFrame(C)
C.to_csv(total+'box_total_20170602031643_supplemented.csv')


# ===================================================================

flist=sorted(glob.glob('E:/pointilism/*.csv'))
day=['2017-02-13','2017-04-01','2017-04-13','2017-04-29','2017-05-07','2017-05-18','2017-05-27','2017-06-02']
for i in range(8):
    globals()['A{}'.format(i)]=pd.read_csv(flist[i], header=None, index_col=False)
    globals()['A{}'.format(i)]=np.array(globals()['A{}'.format(i)])

plt.rcParams['font.family']='tahoma'    
plt.figure(figsize=(10, 13), dpi=75)
M=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')
M.drawcoastlines()
M.drawmapboundary(color='#000000', linewidth=2)
M.fillcontinents(color='#000000')
M.drawparallels(np.arange(26, 41, 2), labels=[1, 0, 0, 0], size=22)
M.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=22)
for i in range(8):
    globals()['xt{}'.format(i)], globals()['yt{}'.format(i)]=\
        M(globals()['A{}'.format(i)][:,0], globals()['A{}'.format(i)][:,1])
    globals()['st{}'.format(i)]=M.scatter(globals()['xt{}'.format(i)], globals()['yt{}'.format(i)], s=1)
# M.scatter(xt, yt, c='#B7BD04', s=4)
# if flist[i][26:32]=='170213' or\
#    flist[i][26:32]=='170401' or\
#    flist[i][26:32]=='180504' or\
#    flist[i][26:32]=='190313':
#    M.scatter(xt, yt, c='#B46404', s=40)
# else:
#     M.scatter(xt, yt, c='#B46404', s=1)
# plt.title(Sargassum horneri 2017, fontsize=30)
plt.tight_layout() # reduce white space layout.
plt.legend([st0, st1, st2, st3, st4, st5, st6, st7], [day[0], day[1], day[2], day[3], day[4], day[5], day[6], day[7]],\
           fontsize=22, markerscale=22, loc=1)
plt.savefig('E:/pointilism/'+'2017_all_final.png')
plt.show()

# =================================================================

day2=['2018-03-28','2018-04-20','2018-05-04']
for i in range(8, 11):
    globals()['A{}'.format(i)]=pd.read_csv(flist[i], header=None, index_col=False)
    globals()['A{}'.format(i)]=np.array(globals()['A{}'.format(i)])

plt.rcParams['font.family']='tahoma'    
plt.figure(figsize=(10, 13), dpi=75)
M=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')
M.drawcoastlines()
M.drawmapboundary(color='#000000', linewidth=2)
M.fillcontinents(color='#000000')
M.drawparallels(np.arange(26, 41, 2), labels=[1, 0, 0, 0], size=22)
M.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=22)
for i in range(8, 11):
    globals()['xt{}'.format(i)], globals()['yt{}'.format(i)]=\
        M(globals()['A{}'.format(i)][:,0], globals()['A{}'.format(i)][:,1])
    globals()['st{}'.format(i)]=M.scatter(globals()['xt{}'.format(i)], globals()['yt{}'.format(i)], s=1)
# M.scatter(xt, yt, c='#B7BD04', s=4)
# if flist[i][26:32]=='170213' or\
#    flist[i][26:32]=='170401' or\
#    flist[i][26:32]=='180504' or\
#    flist[i][26:32]=='190313':
#    M.scatter(xt, yt, c='#B46404', s=40)
# else:
#     M.scatter(xt, yt, c='#B46404', s=1)
# plt.title(Sargassum horneri 2017, fontsize=30)
plt.tight_layout() # reduce white space layout.
plt.legend([st8, st9, st10], [day2[0], day2[1], day2[2]], fontsize=22, markerscale=22, loc=1)
plt.savefig('E:/pointilism/'+'2018_all_final.png')
plt.show()

# =================================================================
day3=['2019-03-13', '2019-04-01', '2019-05-03']
for i in range(11, 14):
    globals()['A{}'.format(i)]=pd.read_csv(flist[i], header=None, index_col=False)
    globals()['A{}'.format(i)]=np.array(globals()['A{}'.format(i)])

plt.rcParams['font.family']='tahoma'    
plt.figure(figsize=(10, 13), dpi=75)
M=Basemap(projection='mill', llcrnrlat=25, urcrnrlat=41, llcrnrlon=117, urcrnrlon=131, resolution='h')
M.drawcoastlines()
M.drawmapboundary(color='#000000', linewidth=2)
M.fillcontinents(color='#000000')
M.drawparallels(np.arange(26, 41, 2), labels=[1, 0, 0, 0], size=22)
M.drawmeridians(np.arange(116, 131, 2), labels=[0, 0, 0, 1], size=22)
for i in range(11, 14):
    globals()['xt{}'.format(i)], globals()['yt{}'.format(i)]=\
        M(globals()['A{}'.format(i)][:,0], globals()['A{}'.format(i)][:,1])
    globals()['st{}'.format(i)]=M.scatter(globals()['xt{}'.format(i)], globals()['yt{}'.format(i)], s=1)
# M.scatter(xt, yt, c='#B7BD04', s=4)
# if flist[i][26:32]=='170213' or\
#    flist[i][26:32]=='170401' or\
#    flist[i][26:32]=='180504' or\
#    flist[i][26:32]=='190313':
#    M.scatter(xt, yt, c='#B46404', s=40)
# else:
#     M.scatter(xt, yt, c='#B46404', s=1)
# plt.title(Sargassum horneri 2017, fontsize=30)
plt.tight_layout() # reduce white space layout.
plt.legend([st11, st12, st13], [day3[0], day3[1], day3[2]], fontsize=22, markerscale=22, loc=1)
plt.savefig('E:/pointilism/'+'2019_all_final.png')
plt.show()