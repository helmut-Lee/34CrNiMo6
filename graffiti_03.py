#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:25:53 2021

@author: Helmut.J.Lee
"""
#3. concatenating 10 years data

import pandas as pd, os

path='E:/remembernokorean/python/kma_buoy_marado_2011-2020/' # Windows
#path='/home/helmut/USB/remembernokorean/python/kma_buoy_marado_2011-2020/' # Linux
flist=sorted(os.listdir(path))
col_name=['station', 'date', 'winds', 'winddeg', 'GUST', 'airpress', 'humid', 'airtemp',\
          'sst', 'maxwave', 'sigwave', 'meanwave', 'wavesec', 'wavedeg']

A=pd.read_csv(path+flist[0], sep=',', header=0, names=col_name, index_col=False)
    
for i in range(8):    
    B=pd.read_csv(path+flist[i+1], sep=',', header=0, names=col_name, index_col=False)
    A=pd.concat([A, B], axis=0, join='outer', ignore_index=True)
        
A['date'][:]=pd.to_datetime(A['date'][:], format='%Y-%m-%d %H:%M')

A.to_csv(path_or_buf='E:/remembernokorean/python/marado_2011~2020.csv', index=False)
