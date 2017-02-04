import sys
sys.path.append('..')

import os
#import pytest
from dummydata import DummyData, Model3

import tempfile


def test_DummyData_init():
        fname = tempfile.mktemp(suffix='.nc')
        d = DummyData(fname, start_year=2000, stop_year=2003, var='ta')
        os.remove(fname)

#~ class TestModel3:
    #~ def setup(self):
        #~ self.m = Model3(start_year=2000, stop_year=2003, var='ta')
#~
    #~ def teardown(self):
        #~ self.m.close()
        #~ os.remove("DummyM3.nc")
#~
    #~ def test_init(self):
        #~ assert self.m.month == 2
        #~ assert self.m.var == 'dummyVariable'

    #~ @pytest.mark.parametrize("test_input", [
        #~ ('lat'),
        #~ ('lon'),
        #~ ('time'),
        #~ ('plev'),
    #~ ])
    #~ def test_createM3Dimension(self,test_input):
        #~ self.m.createM3Dimension()
        #~ assert test_input in self.m.dimensions.keys()

    #~ @pytest.mark.parametrize("test_input,expected", [
        #~ ('lat','latitude'),
        #~ ('lon','longitude'),
        #~ ('time','time'),
        #~ ('plev','pressure'),
    #~ ])
    #~ def test_createM3Variable(self,test_input,expected):
        #~ self.m.createM3Dimension()
        #~ self.m.createM3Variable()
        #~ assert self.m.variables[test_input].long_name == expected
#~
    #~ @pytest.mark.parametrize("test_input,expected", [
        #~ ('lat',96),
        #~ ('lon',144),
        #~ ('time',2),
        #~ ('plev',17),
        #~ ('dummyVariable',2),
    #~ ])
    #~ def test_addM3Data(self,test_input,expected):
        #~ self.m.createM3Dimension()
        #~ self.m.createM3Variable()
        #~ self.m.addM3Data()
        #~ assert len(self.m.variables[test_input]) == expected


