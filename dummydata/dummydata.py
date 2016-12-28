from netCDF4 import Dataset

class DummyData(Dataset):
    """ A Generator for dummy data based on the netCDF4 Dataset class.

    Attributes:
        dim:    spatial dimension
    Methods:

    """
    def __init__(self,filename):
        """ Return Generator object with given size
        """
        Dataset.__init__(
                self,
                filename,
                mode="w",
                format="NETCDF3_CLASSIC")


