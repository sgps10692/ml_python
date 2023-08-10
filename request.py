import requests
import json

form_data = {
    'name': 'nueva generación',
    'city': 'bogotá',
    'location': 'Ciudad bolivar',
    'latitude': '3445',
    'length': '4455',
    'altitude': '34'
}

form_frost_data = {
    'location_id' : '1',
    'probability' : '80'
}

dataJson  = json.dumps(form_data)

dataFrostJson  = json.dumps(form_frost_data)

cabeceras =  {
    'Content-Type' : 'application/json',
    'Accept' : 'application/json'
}
resp = requests.post('http://127.0.0.1:8000/api/forecast_frosts', data=dataFrostJson, headers=cabeceras)

print (resp)