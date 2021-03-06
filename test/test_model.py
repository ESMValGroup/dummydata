# -*- coding: utf-8 -*-

from __future__ import print_function

import unittest
from netCDF4 import netcdftime
import netCDF4

import sys
sys.path.append('..')

from dummydata import Model3, Model2
import tempfile
import os


class TestData(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        tfile = tempfile.mktemp(suffix='.nc')
        Model3(start_year=2000,stop_year=2015, oname=tfile)  # object can not be used further as file is closed!
        self.assertTrue(os.path.exists(tfile))
        os.remove(tfile)

    def test_coordinates(self):
        tfile = tempfile.mktemp(suffix='.nc')

        # 1D case
        Model3(start_year=2000,stop_year=2015, oname=tfile)  # object can not be used further as file is closed!
        self.assertTrue(os.path.exists(tfile))

        F = netCDF4.Dataset(tfile, 'r')
        self.assertEqual(F.variables['lon'].ndim, 1)
        self.assertEqual(F.variables['lat'].ndim, 1)
        F.close()
        os.remove(tfile)

        # 2D case
        Model3(start_year=2000,stop_year=2015, oname=tfile, append_coordinates=True)  # object can not be used further as file is closed!
        self.assertTrue(os.path.exists(tfile))
        F = netCDF4.Dataset(tfile, 'r')
        self.assertEqual(F.variables['lon'].ndim, 2)
        self.assertEqual(F.variables['lat'].ndim, 2)
        F.close()
        os.remove(tfile)

    def tests_cellarea(self):
        tfile = tempfile.mktemp(suffix='.nc')

        # 1D case --> should automatically become 2D
        Model3(start_year=2000,stop_year=2015, oname=tfile, append_cellsize=True)
        F = netCDF4.Dataset(tfile, 'r')
        self.assertEqual(F.variables['lon'].ndim, 2)
        self.assertEqual(F.variables['lat'].ndim, 2)

        self.assertTrue('areacello' in F.variables.keys())
        self.assertEqual(F.variables['areacello'].ndim, 2)

        F.close()

        os.remove(tfile)

    def test_size(self):
        def get_size(f):
            print(f)
            F = netCDF4.Dataset(f, 'r')

            ny = F.dimensions['lat'].size
            nx = F.dimensions['lon'].size
            F.close()
            return ny, nx

        #standard size
        tfile = tempfile.mktemp(suffix='.nc')
        Model2(start_year=2000,stop_year=2015, oname=tfile)
        ny,nx = get_size(tfile)
        self.assertEqual(ny, 96)
        self.assertEqual(nx, 144)
        os.remove(tfile)

        #tiny
        tfile = tempfile.mktemp(suffix='.nc')
        Model2(start_year=2000,stop_year=2015, oname=tfile,size='tiny')
        ny,nx = get_size(tfile)
        self.assertEqual(ny, 18)
        self.assertEqual(nx, 36)
        os.remove(tfile)

        #medium
        tfile = tempfile.mktemp(suffix='.nc')
        Model2(start_year=2000,stop_year=2015, oname=tfile,size='medium')
        ny,nx = get_size(tfile)
        self.assertEqual(ny, 180)
        self.assertEqual(nx, 360)
        os.remove(tfile)

    def test_time(self):

        def get_time_info(f):
            print(f)
            # read netcdf file and extract time information

            F = netCDF4.Dataset(f,'r')
            t = F.variables['time']
            tmp = netcdftime.utime(t.units, calendar=t.calendar)
            d = tmp.num2date(t[:])
            print(len(d), d[0], d[-1])
            F.close()
            return len(d), d[0], d[-1]

        tfile1 = tempfile.mktemp(suffix='.nc')
        Model2(start_year=2001,stop_year=2004, oname=tfile1)
        n, t1, t2 = get_time_info(tfile1)
        self.assertEqual(n, 4*12)
        self.assertEqual(t1.year, 2001)
        self.assertEqual(t1.month, 1)
        self.assertEqual(t1.day, 16)
        self.assertEqual(t2.year, 2004)
        self.assertEqual(t2.month, 12)
        self.assertEqual(t2.day, 16)
        os.remove(tfile1)

        tfile2 = tempfile.mktemp(suffix='.nc')
        Model3(start_year=1998,stop_year=2002, oname=tfile2)
        n, t1, t2 = get_time_info(tfile2)
        self.assertEqual(n, 5*12)
        self.assertEqual(t1.year, 1998)
        self.assertEqual(t1.month, 1)
        self.assertEqual(t1.day, 16)
        self.assertEqual(t2.year, 2002)
        self.assertEqual(t2.month, 12)
        self.assertEqual(t2.day, 16)
        os.remove(tfile2)

    def test_time_bnds(self):
        """Test the values of the `time_bnds` variable."""
        def get_time_bnds_as_datetime(filename):
            """Return `time_bnds` as a list of lists of datetime objects."""
            with netCDF4.Dataset(filename, mode='r') as ncdata:
                var = ncdata.variables['time']
                conv = netcdftime.utime(var.units, calendar=var.calendar)
                var = ncdata.variables['time_bnds']
                time_bnds = conv.num2date(var[:])
                return time_bnds

        with tempfile.NamedTemporaryFile(mode='r', suffix='.nc') as tfile:
            filename = tfile.name
            Model2(start_year=2001, stop_year=2004, oname=filename)
            time_bnds = get_time_bnds_as_datetime(filename)

            self.assertEqual(len(time_bnds), 4*12)

            start, end = time_bnds[0]
            self.assertEqual(start.year, 2001)
            self.assertEqual(start.month, 1)
            self.assertEqual(start.day, 1)
            self.assertEqual(end.year, 2001)
            self.assertEqual(end.month, 2)
            self.assertEqual(end.day, 1)

            start, end = time_bnds[-1]
            self.assertEqual(start.year, 2004)
            self.assertEqual(start.month, 12)
            self.assertEqual(start.day, 1)
            self.assertEqual(end.year, 2005)
            self.assertEqual(end.month, 1)
            self.assertEqual(end.day, 1)


if __name__ == '__main__':
    unittest.main()
