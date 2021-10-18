#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 00:55:32 2021

@author: Helmut
"""
#8. scatter plot for chemistry_9

import numpy as np, pandas as pd, matplotlib.pyplot as plt

path='G:/remembernokorean/python/'

col_name=['ID', 'Y', 'X']
data=pd.read_csv(path+'bamford data.csv', header=0, names=col_name, index_col=False)

plt.figure(figsize=(3, 6), dpi=200)
plt.scatter(data['X'], data['Y'], color='#ff0000', s=10)
plt.xlabel('Rotation Velocity(log scale)')
plt.ylabel('Magnitude')
plt.xlim(1.4, 2.6), plt.ylim(-24, -15)
plt.xticks(ticks=np.arange(1.4, 2.6, 0.2))