# -*- coding: utf-8 -*-

#~ import datetime
import unittest
#~ from netCDF4 import netcdftime
#~ import netCDF4

import sys
sys.path.append('..')

from dummydata import Metadata
#~ import tempfile
#~ import os


class TestData(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def test_init(cls):
        Metadata('ta')

    def test_attr(self):
        M = Metadata('ta')
        self.assertEqual(M.units, 'K')
        self.assertEqual(M.standard_name, 'air_temperature')
        self.assertEqual(M.long_name, 'Air temperature')
        self.assertEqual(M.original_name, 'T,PS')
        self.assertEqual(M.comment, 'T interpolated to standard plevs')

        # test for invalid attribute





if __name__ == '__main__':
    unittest.main()
