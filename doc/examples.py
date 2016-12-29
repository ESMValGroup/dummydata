import sys
sys.path.append('..')

from dummydata import Model3, Model2

# generate a 3D variable
M3 = Model3(start_year=2000,stop_year=2015)

# generate a 2D variable
M2 = Model2(start_year=2003,stop_year=2014)
M2 = Model2(method='constant', constant=5., oname='myconst5',start_year=1998,stop_year=2002)
