from flask import Flask
from flask import request
from flask_restful import Api
import pandas as pd
import json
from types import SimpleNamespace

import forecastfun

app = Flask(__name__)

@app.route('/forecast', methods = ['POST'])
def forecast():
    data = request.get_json(silent=True)
    d = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
        
    weather = data['weather']       
    weather = pd.DataFrame.from_dict(weather)   
    weather.set_index('dt', inplace = True)        
        
    result = forecastfun.pvlib_forecast(d.location.latitude, 
                                  d.location.longitude,
                                  d.location.timezone, 
                                  d.param.mod_pdc0, 
                                  d.param.mod_gamma_pdc, 
                                  d.param.inv_pdc0, 
                                  weather)
    
    return result.to_dict(), 200

