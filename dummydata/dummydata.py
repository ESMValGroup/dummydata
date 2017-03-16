from netCDF4 import Dataset
import numpy as np
from netCDF4 import netcdftime
import datetime
from dateutil import relativedelta

from .meta import Metadata


class DummyData(Dataset):
    """ A Generator for dummy data based on the netCDF4 Dataset class.

    Attributes:
        dim:    spatial dimension
    Methods:

    """
    def __init__(self,filename, **kwargs):
        """
        Return Generator object with given size
        """
        if filename[-3:] != '.nc':
            filename += '.nc'

        Dataset.__init__(
                self,
                filename,
                mode="w",
                format="NETCDF3_CLASSIC")

        self.method = kwargs.pop('method', 'uniform')
        self.start = kwargs.pop('start_year', -99)
        self.stop = kwargs.pop('stop_year', -99)
        assert self.start > 0, 'Start date needs to be given!'
        assert self.stop > 0, 'Stop date needs to be given!'
        assert self.stop >= self.start
        self.month = (self.stop-self.start+1)*12  # number of monthly timesteps

        if self.method == 'constant':
            constant = kwargs.pop('constant', None)
            assert constant is not None, 'ERROR: constant value needs to be provided when this method is chosen'
            self.constant = constant

        self._define_size(kwargs.get('size', None))

        # specifies if coordinate and cell area fields should be appended to output file as 2D fields
        self._append_coordinates = str(kwargs.get('append_coordinates', False))  # as string, as bool attributes not supported by netCDF4 library
        self._append_cellsize = str(kwargs.get('append_cellsize', False))
        if self._append_cellsize == 'True':
            self._append_coordinates = 'True'  # cellsize only supported when coordinates in 2D


    def _define_size(self, s):
        if s is None:
            # set default size 1.875 x 2.5 deg
            self.ny = 96
            self.nx = 144
            return

        if s == 'medium':  # 1x1 deg
            self.ny = 180
            self.nx = 360
        elif s == 'small': # 5x5 deg
            self.ny = 180/5
            self.nx = 360/5
        elif s == 'tiny':  # 10x10 deg
            self.ny = 180/10
            self.nx = 360/10
        else:
            assert False, 'Unknown size! ' + s


    def _create_time_dimension(self):
        self.createDimension('time', None)

    def _create_coordinate_dimensions(self):
        self.createDimension('lat', self.ny)
        self.createDimension('lon', self.nx)

    def _create_bnds_dimensions(self):
        self.createDimension('bnds', 2)


    def _create_time_variable(self):
        self.createVariable('time', 'f8', ('time',))
        self.createVariable('time_bnds', 'f8', ('time', 'bnds',))
        self.variables['time'].units = 'days since 1850-01-01 00:00:00'
        self.variables['time'].bounds = 'time_bnds'
        self.variables['time'].calendar = 'standard'
        self.variables['time'].axis = 'T'
        self.variables['time'].long_name = 'time'
        self.variables['time'].standard_name = 'time'

    def _create_coordinates(self):

        if self._append_coordinates == 'True':  # 2D coordinate fields
            self.createVariable('lat', 'f8', ('lat','lon', ))
            self.createVariable('lon', 'f8', ('lat','lon', ))
        else:  # 1D
            self.createVariable('lat', 'f8', ('lat',))
            self.createVariable('lon', 'f8', ('lon',))

        #~ self.variables['lat'].bounds = 'lat_bnds'
        self.variables['lat'].units = 'degrees_north'
        self.variables['lat'].axis = 'Y'
        self.variables['lat'].long_name = 'latitude'
        self.variables['lat'].standard_name = 'latitude'

        #~ self.variables['lon'].bounds = 'lon_bnds'
        self.variables['lon'].units = 'degrees_east'
        self.variables['lon'].axis = 'X'
        self.variables['lon'].long_name = 'longitude'
        self.variables['lon'].standard_name = 'longitude'

    #~ def _create_coordinates_1D(self):
        #~ self.createVariable('lat', 'f8', ('lat',))
        #~ self.createVariable('lat_bnds', 'f8', ('lat', 'bnds',))
        #~ self.createVariable('lon', 'f8', ('lon',))
        #~ self.createVariable('lon_bnds', 'f8', ('lon', 'bnds',))



    def add_ancillary_data(self):
        """
        add ancillary fields like 2D fields fo coordinates and cellsize
        """
        if self._append_cellsize == 'True':
            self.createVariable('areacello', 'f8', ('lat','lon', ))
            self.variables['areacello'][:,:] = np.ones((self.ny,self.nx))


    def _set_time_data(self):
        tmp = netcdftime.utime(self.variables['time'].units, calendar=self.variables['time'].calendar)
        d = [datetime.datetime(self.start,1,1) + relativedelta.relativedelta(months=x) for x in range(0, self.month)]
        self.variables['time'][:]=tmp.date2num(d)

    def _set_coordinate_data(self):
        lat = np.arange(-90., 90., 180./self.ny).astype('float')  # todo is this correct ??
        lon = np.arange(-180., 180., 360./self.nx).astype('float') #* (360. / 144.)


        if self._append_coordinates == 'True': # 2D
            LAT,LON = np.meshgrid(lat,lon)
            self.variables['lat'][:,:] = LAT
            self.variables['lon'][:,:] = LON
        else: # 1D
            self.variables['lat'][:] = lat
            self.variables['lon'][:] = lon




        #~ self.variables['lat_bnds'][:, 0] = self.variables[
            #~ 'lat'][:] - (180. / 95. / 2.)
        #~ self.variables['lat_bnds'][:, 1] = self.variables[
            #~ 'lat'][:] + (180. / 95. / 2.)

        #~ self.variables['lon_bnds'][:, 0] = self.variables[
            #~ 'lon'][:] - (360. / 144. / 2.)
        #~ self.variables['lon_bnds'][:, 1] = self.variables[
            #~ 'lon'][:] + (360. / 144. / 2.)


    def _set_metadata(self):

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


    def _set_variable_metadata(self):

        M = Metadata(self.var)

        self.variables[self.var].standard_name = M.standard_name
        self.variables[self.var].long_name = M.long_name
        self.variables[self.var].units = M.units
        self.variables[self.var].original_name = M.original_name
        self.variables[self.var].comment = M.comment

        self.variables[self.var].cell_methods = 'time: mean (interval: 30 days)'
        self.variables[self.var].cell_measures = 'area: areacella'
        self.variables[self.var].history = ''
        self.variables[self.var].missing_value = 1.e+20


    def _get_variable_data(self):
        if self.method == 'uniform':
            return np.random.uniform(
                size=(self.month,) + self.variables[self.var].shape[1:])
        elif self.method == 'constant':
            return np.ones((self.month,) + self.variables[self.var].shape[1:])*self.constant


        else:
            assert False

