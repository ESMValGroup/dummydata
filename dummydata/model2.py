from dummydata import DummyData

import numpy

class Model2(DummyData):
    """
    Dummydata that mimic Model data with two spatial dimensions
    """
    def __init__(self,var='dummyVariable2d', month = 3, oname="DummyM2.nc", **kwargs):
        """
        create an empty 3D file

        Parameters
        ----------
        month : int
            number of months
        var : str
            variable name to specify
        """
        super(Model2, self).__init__(oname, **kwargs)

        self.month = month
        self.var = var

        self.createM2Dimension()
        self.createM2Variable()
        self.addM2Data()
        self.close()

    def createM2Dimension(self):
        self._create_time_dimension()
        self._create_coordinate_dimensions()
        self._create_bnds_dimensions()

    def createM2Variable(self):
        # create time variable
        self._create_time_variable()

        # create coordinates
        self._create_coordinates()

        self.createVariable(
            self.var,
            'f4',
            ('time',
             'lat',
             'lon',
             ),
            fill_value=1.e+20)

        self.variables[self.var].standard_name = 'air_temperature'
        self.variables[self.var].long_name = 'Air Temperature'
        self.variables[self.var].units = 'K'
        self.variables[self.var].original_name = 'T,PS'
        self.variables[self.var].comment = 'T interpolated to standard plevs'
        self.variables[self.var].cell_methods = 'time: mean (interval: 30 days)'
        self.variables[self.var].cell_measures = 'area: areacella'
        self.variables[self.var].history = ''
        self.variables[self.var].missing_value = 1.e+20

    def addM2Data(self):
        # set variable data
        self.variables[self.var][0:self.month, :, :] = self._get_variable_data()

        # set coordinates
        self._set_coordinate_data()

        # set the time
        self._set_time_data()
