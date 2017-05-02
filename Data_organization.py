#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:29:36 2017

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
datafiles = glob('*.DAT')

ndim = 9450336
xdimension = range(0, 3936)
ydimension = range(0, 2401) 
#zdimension = 35
                                                        
#dimensions
#time = nc.createDimension('time', None)
x = nc.createDimension('x', len(xdimension))
y = nc.createDimension('y', len(ydimension))
time = nc.createDimension('time', len(datafiles))
#nc.createDimension('z', zdimension)
                                                        
#variables
x = nc.createVariable('x', 'f4', ('x',))
y = nc.createVariable('y', 'f4', ('y',))
time = nc.createVariable('time', 'f4', ('time',))
#z = nc.createVariable('z', 'f4', ('z',))
nc.createVariable('field', 'f4', ('y', 'x', 'time'))

t_scan = []
i = 0
for datafile in datafiles:
    z1D = np.fromfile(datafile, dtype=np.float32)
    z = np.reshape(z1D, (-1, 3936))
    z[z == -9999] = np.nan # no data handling
    z = np.flipud(z) # flip top to bottom
    nc.variables['field'][i] = z
    #plt.imshow(z)
    #plt.show()
    print datafile
    t_scan.append(int(datafile.split('TopoDat_')[1].split('.')[0]))
    i += 1

nc.variables['x'][:] = np.arange(0, len(x)*1E-3, 1E-3)
nc.variables['y'][:] = np.arange(0, len(y)*1E-3, 1E-3)
nc.variables['time'][:] = np.array(t_scan)

x.units = 'Meters'
y.units = 'Meters'


#def write_nc( datafile, varname, x, y):
    #nx = len(x)
    #ny = len(y)
    
#write_nc( datafile, 'data', x, y)

nc.close() 

