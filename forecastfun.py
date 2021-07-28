from pvlib.pvsystem import PVSystem #, retrieve_sam
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
from pvlib.modelchain import ModelChain
from pvlib.location import Location

############# funkcja
def pvlib_forecast(lat, lon, tz, mod_pdc0, mod_gamma_pdc, inv_pdc0, weather):

    temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
    location = Location(lat, lon, tz)
    
    pvwatts_system = PVSystem(
        module_parameters={'pdc0': mod_pdc0, 'gamma_pdc': mod_gamma_pdc},
        inverter_parameters={'pdc0': inv_pdc0},
        temperature_model_parameters=temperature_model_parameters)
    
    mc = ModelChain(pvwatts_system, location,
                    aoi_model='no_loss', spectral_model='no_loss')
    
    mc.run_model_from_effective_irradiance(weather)
    
    return(mc.ac)
############## koniec funkcji
