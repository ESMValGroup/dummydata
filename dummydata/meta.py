class Metadata(object):
    def __init__(self, v):
        self.v = v
        self._set_dict()
        self._set_attributes()

    def _set_dict(self):
        self.dict = {}
        self.dict.update({'ta' : {'standard_name' : 'air_temperature', 'long_name' : 'Air temperature', 'units' : 'K', 'original_name' : 'T,PS', 'comment' : 'T interpolated to standard plevs'}})
        self.dict.update({'pr' : {'standard_name' : 'precipitation', 'long_name' : 'Precipitation', 'units' : 'kg m-2 s-1', 'original_name' : 'P', 'comment' : 'some precipitation'}})
        self.dict.update({'ua' : {'standard_name' : 'xxxxx', 'long_name' : 'xxxxxx', 'units' : 'm s-1', 'original_name' : 'U', 'comment' : 'some wind'}})
        self.dict.update({'mrro' : {'standard_name' : 'runoff_flux', 'long_name' : 'runoff_flux', 'units' : 'kg m-2 s-1', 'original_name' : 'Q', 'comment' : 'some runoff'}})
        self.dict.update({'evspsbl' : {'standard_name' : 'evaporation', 'long_name' : 'evaporation', 'units' : 'kg m-2 s-1', 'original_name' : 'ET', 'comment' : 'some evaporation'}})
        self.dict.update({'et' : {'standard_name' : 'evaporation_mm', 'long_name' : 'evaporation', 'units' : 'mm d-1', 'original_name' : 'ET', 'comment' : 'some evaporation'}})
        self.dict.update({'hfls' : {'standard_name' : 'surface_upward_latent_heat_flux', 'long_name' : 'surface_upward_latent_heat_flux', 'units' : 'W m-2', 'original_name' : 'xxx', 'comment' : 'some xxx'}})
        self.dict.update({'mrsos' : {'standard_name' : 'moisture_content_of_soil_layer', 'long_name' : 'moisture_content_of_soil_layer', 'units' : 'kg m-2', 'original_name' : 'xxx', 'comment' : 'some xxx'}})
        self.dict.update({'sic' : {'standard_name' : 'sea_ice_area_fraction', 'long_name' : 'sea_ice_area_fraction', 'units' : '%', 'original_name' : 'xxx', 'comment' : 'fraction of grid cell covered by sea ice'}})
        self.dict.update({'ts' : {'standard_name' : 'surface_temperature', 'long_name' : 'surface_temperature', 'units' : 'K', 'original_name' : 'surface_temperature', 'comment' : 'surface_temperature'}})

        self.dict.update({'ua' : {'standard_name' : 'windspeed_u', 'long_name' : 'Air windspeed_u', 'units' : 'm s-1', 'original_name' : 'xxxx', 'comment' : 'windspeed_u'}})
        self.dict.update({'va' : {'standard_name' : 'windspeed_v', 'long_name' : 'Air windspeed_v', 'units' : 'm s-1', 'original_name' : 'xxxx', 'comment' : 'windspeed_v'}})



    def _set_attributes(self):
        assert self.v in self.dict.keys(), 'ERROR: metadata for variable ' + self.v + ' is unknown!'

        d = self.dict[self.v]

        self.standard_name = None
        self.long_name = None
        self.units = None
        self.original_name = None
        self.comment = None

        k = 'standard_name'
        if k in d.keys():
            self.standard_name = d[k]

        k = 'long_name'
        if k in d.keys():
            self.long_name = d[k]

        k = 'units'
        if k in d.keys():
            self.units = d[k]

        k = 'original_name'
        if k in d.keys():
            self.original_name = d[k]

        k = 'comment'
        if k in d.keys():
            self.comment = d[k]
