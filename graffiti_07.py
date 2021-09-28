# -*- coding: utf-8 -*-
"""
Created on Thu May  6 17:32:34 2021

@author: Helmut.J.Lee
"""
#7. modify import error(basemap)

# before you read, conda install -c conda-forge proj4
import os
os.environ['PROJ_LIB']='C:/ProgramData/Anaconda3/envs/base2/share/proj' # Windows
#os.environ['PROJ_LIB']='/root/anaconda3/envs/base2/share/proj/' # Linux

from mpl_toolkits.basemap import Basemap


(1*3.1*8000)/58
(1*2.9*8000)/58

(mol/L * 3.1ml * 8000) / (60ml - 2ml)