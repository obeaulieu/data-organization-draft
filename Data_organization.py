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
from numpy import shape


# create a new netCDF file
file = 'BLcontrolscanFiles.nc'
nc = Dataset(file , 'w' , format='NETCDF4')
print (nc.file_format)

#data input                                                       

#gtif = gdal.Open( '/Users/livbeaulieu30/Google Drive/Scan Files/*.DAT' )
#print gtif.GetMetadata()
# a = gtif.GetRasterBand(1).ReadAsArray()
datafiles = glob('/Users/livbeaulieu30/Google Drive/Scan Files/*.DAT')

t_scan = []
for datafile in datafiles:
    z1D = np.fromfile(datafile, dtype=np.float32)
    z = np.reshape(z1D, (-1, 3936))
    z[z == -9999] = np.nan # no data handling
    z = np.flipud(z) # flip top to bottom
    #plt.imshow(z)
    #plt.show()
    print datafile
    t_scan.append(int(datafile.split('TopoDat_')[1].split('.')[0]))

                                                       
ndim = 9450336
xdimension = range(0, 3936)
ydimension = range(0, 2401) 
#zdimension = 35
                                                        
#dimensions
time = nc.createDimension('time', None)
nc.createDimension('x', len(xdimension))
nc.createDimension('y', len(ydimension))
#nc.createDimension('z', zdimension)
                                                        
#variables
time = nc.createVariable('time', 'f8', ('time',))
x = nc.createVariable('x', 'f4', ('x',))
y = nc.createVariable('y', 'f4', ('y',))
#z = nc.createVariable('z', 'f4', ('z',))
field = nc.createVariable('field', 'f8', ('time', 'x', 'y'))
                                                        
x.units = 'Meters'
y.units = 'Meters'


#def write_nc( datafile, varname, x, y):
    #nx = len(x)
    #ny = len(y)
    
#write_nc( datafile, 'data', x, y)

nc.close() 

