#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:57:20 2017

@author: livbeaulieu30
"""

# Data organization
# Using a netCDF to organize photos and scan data from DB1

from netCDF4 import Dataset
import numpy as np
from glob import glob
from osgeo import gdal

gtif = gdal.Open( "/Users/livbeaulieu30/Google Drive/03_Scan0001.TIF" )
print gtif.GetMetadata()

controlscanFiles = sorted(glob('/Users/livbeaulieu30/Google Drive/03_Scan0001.TIF'))

for i in range(len(controlscanFiles)):
    try:
        
            codename = controlscanFiles
            # create a new netCDF file
            ncfile = Dataset('gtif' , 'w' , format='NETCDF4')
            ncfile.description = 'Scan data'
            
            ndim = 120000
            xdimension = 400
            ydimension = 300 
            zdimension = 35
            
            #dimensions
            ncfile.createDimension('time', None)
            ncfile.createDimension('x', xdimension)
            ncfile.createDimension('y', ydimension)
            ncfile.createDimension('z', zdimension)
            
            #variables
            time = ncfile.createVariable('time', 'f8', ('time',))
            x = ncfile.createVariable('x', 'f4', ('x',))
            y = ncfile.createVariable('y', 'f4', ('y',))
            z = ncfile.createVariable('z', 'f4', ('z',))
            field = ncfile.createVariable('field', 'f8', ('time', 'x', 'y', 'z',))
            
            x.units = 'meters'
            y.units = 'meters'
            
            ncfile.close()
    except:
        print 'Critical Error'


