#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:54:21 2021

@author: Helmut.J.Lee
"""
#7. netCDF

import numpy as np
import netCDF4 as nc, matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

path='E:/remembernokorean/matlab/' # Windows
# path='/home/helmut/USB/remembernokorean/matlab/' # Linux

C=nc.Dataset(path+'woa18_A5B7_t00_01.nc', 'r', format='NETCDF4')
# this file is statistical mean of temperature on 1 degree grid for 2005-2017 years.
# mode = 'w'rite, 'r'ead, 'a'dd.

C # similar fuction as ncdump.
C.variables # details of variables.
C.variables.keys()  # variable's name.

lat=C['lat'] # list in list. can't read.
lat=C['lat'][:] # now can read.
lon=C['lon'][:]
depth=C['depth'][:]
t_mn=C['t_mn'][0][0] # current shape=(time, depth, lat, lon)
LON, LAT=np.meshgrid(lon, lat)

plt.figure(figsize=(12,8), dpi=200.0)
D=Basemap(projection='ortho', lon_0=126.5, lat_0=33.5, resolution='h') # lon_0 and lat_0 : center
#D=Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='h')
D.drawcoastlines()
D.fillcontinents(color='#e0e0e0')
xt, yt=D(LON, LAT)
D.pcolor(xt, yt, t_mn, cmap='jet') # parameter 'shading' is available matplotlib version 3.3 or higher.
plt.colorbar(ticks=np.arange(-2, 33 , 2, dtype='int64'), label='Temperature($\circ$C)')
plt.title('Statistical mean for 2005-2017', fontsize=20)

#lat_ko=np.where((lat>=30)&(lat<=50))[0] # list in tuple
#lon_ko=np.where((lon>=120)&(lon<=140))[0]
#lat_s, lon_s=lat[lat_ko],lon[lon_ko]

