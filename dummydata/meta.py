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

        self.dict.update({'sm' : {'standard_name' : 'water content of soil layer', 'long_name' : 'water content of soil layer', 'units' : 'kg m-2', 'original_name' : 'xxxx', 'comment' : 'xxxx'}})

        self.dict.update({'tas' : {'standard_name' : 'near surface temperature', 'long_name' : 'near surface temperature', 'units' : 'K', 'original_name' : 'T', 'comment' : 'xxxxxx'}})

        self.dict.update({'zg' : {'standard_name' : 'geopotential height', 'long_name' : 'geopotential height', 'units' : 'm', 'original_name' : 'GPH', 'comment' : 'xxxxxx'}})

        self.dict.update({'rlut' : {'standard_name' : 'TOA Outgoing Longwave Radiation', 'long_name' : 'TOA Outgoing Longwave Radiation', 'units' : 'W m-2', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})
        self.dict.update({'clt' : {'standard_name' : 'total cloud fraction', 'long_name' : 'total cloud fraction', 'units' : '%', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})

        self.dict.update({'LW_CRE' : {'standard_name' : 'longwave cloud radiative effect', 'long_name' : 'longwave cloud radiative effect', 'units' : 'W m-2', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})
        self.dict.update({'SW_CRE' : {'standard_name' : 'shortwave cloud radiative effect', 'long_name' : 'shortwave cloud radiative effect', 'units' : 'W m-2', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})

        self.dict.update({'hus' : {'standard_name' : 'specific humidity', 'long_name' : 'specific humidity', 'units' : '1', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})
        self.dict.update({'rsut' : {'standard_name' : 'TOA outgoing shortwave radiation', 'long_name' : 'TOA outgoing shortwave radiation', 'units' : 'W m-2', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})

        self.dict.update({'od550aer' : {'standard_name' : 'Ambient Aerosol Optical Thickness at 550 nm', 'long_name' : 'Ambient Aerosol Optical Thickness at 550 nm', 'units' : '1', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})
        self.dict.update({'od870aer' : {'standard_name' : 'Ambient Aerosol Optical Thickness at 870 nm', 'long_name' : 'Ambient Aerosol Optical Thickness at 870 nm', 'units' : '1', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})

        self.dict.update({'abs550aer' : {'standard_name' : 'Ambient Aerosol Absorption Optical Thickness at 550 nm', 'long_name' : 'Ambient Aerosol Absorption Optical Thickness at 550 nm', 'units' : '1', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})

        self.dict.update({'od550lt1aer' : {'standard_name' : 'Ambient Fine Aerosol Optical Thickness at 550 nm', 'long_name' : 'Ambient Fine Aerosol Optical Thickness at 550 nm', 'units' : '1', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})

        self.dict.update({'toz' : {'standard_name' : 'not clear yet', 'long_name' : 'not clear yet', 'units' : '1', 'original_name' : 'xxx', 'comment' : 'xxxxxx'}})







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
