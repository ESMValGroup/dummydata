from dummydata import DummyData

import numpy

class Model3(DummyData):
    """ Dummydata that mimic Model data with three spatial dimensions
    """
    def __init__(self,var='dummyVariable', month = 3):
        """
        create an empty 3D file

        Parameters
        ----------
        month : int
            number of months
        var : str
            variable name to specify
        """
        DummyData.__init__(self,"DummyM3.nc")
        self.month = month
        self.var = var

        self.createM3Dimension()
        self.createM3Variable()
        self.addM3Data()
        self.close()

    def createM3Dimension(self):
        self.createDimension('time', None)
        self.createDimension('plev', 17)
        self.createDimension('lat', 96)
        self.createDimension('lon', 144)
        self.createDimension('bnds', 2)


    def createM3Variable(self):

        # create time variable
        self._create_time_variable()

        # create coordinates
        self._create_coordinates()


        self.createVariable('plev', 'f8', ('plev',))

        self.createVariable(
            self.var,
            'f4',
            ('time',
             'plev',
             'lat',
             'lon',
             ),
            fill_value=1.e+20)


        self.variables['plev'].units = 'Pa'
        self.variables['plev'].axis = 'Z'
        self.variables['plev'].positive = 'down'
        self.variables['plev'].long_name = 'pressure'
        self.variables['plev'].standard_name = 'air_pressure'

        self.variables[self.var].standard_name = 'air_temperature'
        self.variables[self.var].long_name = 'Air Temperature'
        self.variables[self.var].units = 'K'
        self.variables[self.var].original_name = 'T,PS'
        self.variables[self.var].comment = 'T interpolated to standard plevs'
        self.variables[self.var].cell_methods = 'time: mean (interval: 30 days)'
        self.variables[self.var].cell_measures = 'area: areacella'
        self.variables[self.var].history = ''
        self.variables[self.var].missing_value = 1.e+20


        self.institution = 'Test'
        self.institute_id = 'Test'
        self.experiment_id = 'Test'
        self.source = 'Test'
        self.model_id = 'Test'
        self.forcing = 'Test'
        self.parent_experiment_id = 'Test'
        self.parent_experiment_rip = 'Test'
        self.branch_time = 42.
        self.contact = 'Test'
        self.references = 'Test'
        self.initialization_method = 42
        self.physics_version = 42
        self.tracking_id = 'Test'
        self.acknowledgements = 'Test'
        self.cesm_casename = 'Test'
        self.cesm_repotag = 'Test'
        self.cesm_compset = 'Test'
        self.resolution = 'Test'
        self.forcing_note = 'Test'
        self.processed_by = 'Test'
        self.processing_code_information = 'Test'
        self.product = 'Test'
        self.experiment = 'Test'
        self.frequency = 'Test'
        self.creation_date = 'Test'

        self.history = 'Test'
        self.Conventions = 'Test'
        self.project_id = 'Test'
        self.table_id = 'Test'
        self.title = 'Test'
        self.parent_experiment = 'Test'
        self.modeling_realm = 'Test'
        self.realization = 42
        self.cmor_version = 'Test'

    def addM3Data(self):
        self.variables['plev'][:] = [
            100000,
            92500,
            85000,
            70000,
            60000,
            50000,
            40000,
            30000,
            25000,
            20000,
            15000,
            10000,
            7000,
            5000,
            3000,
            2000,
            1000]


        self.variables[self.var][0:self.month, :, :, :] = numpy.random.uniform(
            size=(self.month,) + self.variables[self.var].shape[1:])

        # set coordinates
        self._set_coordinate_data()

        # set the time
        self._set_time_data()


