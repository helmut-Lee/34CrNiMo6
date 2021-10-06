#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:20:08 2021

@author: Helmut.J.Lee
"""
#4. seperate A

import pandas as pd, numpy as np, os, sys
sys.path.append('/home/helmut/USB/remembernokorean/python/shc/mara/')
path='/home/helmut/USB/remembernokorean/python/shc/kma_buoy_marado_2011-2020/' # Linux

flist=sorted(os.listdir(path))
col_name=['station', 'date', 'winds', 'winddeg', 'GUST', 'airpress', 'humid', 'airtemp',\
          'sst', 'maxwave', 'sigwave', 'meanwave', 'wavesec', 'wavedeg']

A=pd.read_csv(path+flist[0], sep=',', header=0, names=col_name, index_col=False)    
for i in range(8):    
    B=pd.read_csv(path+flist[i+1], sep=',', header=0, names=col_name, index_col=False)
    A=pd.concat([A, B], axis=0, join='outer', ignore_index=True)
    
A['date'][:]=pd.to_datetime(A['date'][:], format='%Y-%m-%d %H:%M')

# A=A.*** == inplace=True

A.set_index(A['date'], inplace=True)
A.drop(['station', 'winddeg'], axis=1, inplace=True)
A.dropna(inplace=True)
A.describe()

A.count()

A['2011-01-01 00:00:00']


testx=np.load('/home/helmut/USB/remembernokorean/python/shc/mara/test_x.npy', allow_pickle=True)
trainx=np.load('/home/helmut/USB/remembernokorean/python/shc/mara/train_x.npy', allow_pickle=True)
