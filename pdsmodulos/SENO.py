#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Humberto Delgado

Descripcion: Funcion senoidal

argumentos: Vmax = amplitud maxima
            dc   = nivel de continua
            ff   = frecuencia
            N    = cantidad de muestras
            Fs   = frecuencia de Muestreo (Nyquist)
retorna = 

"""
#%%  inicialiizacion modulos

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#import pdsmodulos as pds #carpeta contenedoras de funciones/modulos 



#½½

def SENO( vmax=1, dc=0, ff=1, N =100, ph=0, FS=1000.0):
    
    Ts=1/FS  #tiempo de muestreo
    
   
   #grilla eje temporal

    x1=np.linspace(0, (N-1), N).flatten()
    
    y1=dc + vmax*np.sin(2*np.pi*x1*ff*Ts + ph).flatten()

    
    
     
    return x1,y1


#%%   
     
#x,y=SENO(vmax=2, dc=1, ff=10, N=1000)
    
#plt.plot(x, y, 'red' )
    
    
    
    
   