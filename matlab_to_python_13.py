#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:03:39 2021

@author: Helmut.J.Lee
"""

#13. Grouped bar chart

import numpy as np, pandas as pd, matplotlib.pyplot as plt

stat=pd.read_csv('F:/remembernokorean/bachelor\'s degree/tide_buoy_statistic.csv', header=None, index_col=False)
stat=np.array(stat)
tide, buoy=stat[:12, :], stat[17, :]

tide_mean=np.mean(tide, axis=0)
label, label2=['Jeju', 'Moseulpo', 'Anheung'], ['Chujado', 'Marado', 'Seogwipo']

plt.rcParams['font.family']='tahoma'
plt.rcParams['font.size']=16
plt.rcParams['figure.figsize']=(16, 8) # ==plt.figure(figsize)
plt.rcParams['figure.dpi']=100 # ==plt.figure(dpi)
plt.rcParams['figure.autolayout']=True # ==plt.tight_layout()

ax1=plt.subplot(1, 2, 1)
b0=plt.bar(0.5, buoy[0], width=0.4, color='#D98880', zorder=20)
b1=plt.bar(1, buoy[1], width=0.4, color='#C39BD3', zorder=20)
b2=plt.bar(1.5, buoy[2], width=0.4, color='#76D7C4', zorder=20)
plt.bar(2.5, buoy[3], width=0.4, color='#D98880', zorder=20)
plt.bar(3, buoy[4], width=0.4, color='#C39BD3', zorder=20)
plt.bar(3.5, buoy[5], width=0.4, color='#76D7C4', zorder=20)
plt.bar(4.5, buoy[6], width=0.4, color='#D98880', zorder=20)
plt.bar(5, buoy[7], width=0.4, color='#C39BD3', zorder=20)
plt.bar(5.5, buoy[8], width=0.4, color='#76D7C4', zorder=20)
plt.grid(axis='y', linestyle='--', zorder=0)
plt.legend([b0, b1, b2], ['2017', '2018', '2019'], loc=1)
plt.xlim(0, 6), plt.ylim(0, 1.23)
plt.xticks(np.arange(1, 5.1, 2), labels=label2, fontsize=24), plt.yticks(np.arange(0, 1.1, 0.1))
plt.ylabel('Correlation Coefficient', fontsize=24)
plt.text(2, 1.1, 'Buoy', fontsize=30)

ax2=plt.subplot(1, 2, 2, sharey=ax1)
t0=plt.bar(0.5, tide_mean[0], width=0.4, color='#7B241C', zorder=20) # zorder : layer sequence
t1=plt.bar(1, tide_mean[1], width=0.4, color='#633974', zorder=20)
t2=plt.bar(1.5, tide_mean[2], width=0.4, color='#117864', zorder=20)
plt.bar(2.5, tide_mean[3], width=0.4, color='#7B241C', zorder=20)
plt.bar(3, tide_mean[4], width=0.4, color='#633974', zorder=20)
plt.bar(3.5, tide_mean[5], width=0.4, color='#117864', zorder=20)
plt.bar(4.5, tide_mean[6], width=0.4, color='#7B241C', zorder=20)
plt.bar(5, tide_mean[7], width=0.4, color='#633974', zorder=20)
plt.bar(5.5, tide_mean[8], width=0.4, color='#117864', zorder=20)
plt.grid(axis='y', linestyle='--', zorder=0)
plt.legend([t0, t1, t2], ['2017', '2018', '2019'], loc=1)
plt.xlim(0, 6), plt.ylim(0, 1.23)
plt.xticks(np.arange(1, 5.1, 2), labels=label, fontsize=24), plt.yticks(np.arange(0, 1.1, 0.1), visible=False)
plt.text(2, 1.1, 'Tide', fontsize=30)


# CD313A, 0047A0