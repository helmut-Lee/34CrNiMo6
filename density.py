#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:22:34 2020

@author: helmut
"""

def roms_eos(s,t,p):
    b0 =  8.24493e-1
    b1 = -4.0899e-3
    b2 =  7.6438e-5
    b3 = -8.2467e-7
    b4 =  5.3875e-9
    
    c0 = -5.72466e-3
    c1 = +1.0227e-4
    c2 = -1.6546e-6
    
    d0 = 4.8314e-4
    
    a0 = 999.842594
    a1 =   6.793952e-2
    a2 =  -9.095290e-3
    a3 =   1.001685e-4
    a4 =  -1.120083e-6
    a5 =   6.536332e-9
    
    T68 = t * 1.00024;
    densA = a0+(a1+(a2+(a3+(a4+a5*T68)*T68)*T68)*T68)*T68
    
    dens = densA+(b0+(b1+(b2+(b3+b4*T68)*T68)*T68)*T68)*s+(c0+(c1+c2*T68)*T68)*s*(s**0.5)+d0*s**2 - 1000
    return dens

def simple_eos(s,t,p):
    densB=27+(-0.15*(t-10))+(0.78*(s-35))+(4.5*(10^-3)*p)
    return densB