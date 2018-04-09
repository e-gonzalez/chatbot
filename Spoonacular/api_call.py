import json
import requests
import urllib

token = "YHvCM9V4j6mshPALYJaOfAvCgZJWp1jiSoOjsn93w0PY8v7ibw"

def spoonacular_api_call( method, url, parameters):
    #Param payload es para los 'POST'
    """
    :param instruction:
    :param method:
    :param url:
    :param token: <str>
    :param payload:  
    :param parameters:
    :return:
    """
    headers = {"X-Mashape-Key": token,
               'Accept': 'application/json',
                }
        
    if method.upper() == 'GET':
        encoded_parameters = urllib.urlencode(parameters)
        url = url + encoded_parameters
        response = requests.get(url, headers=headers)

    else : #method.upper() == 'POST':
        response = requests.post(url, headers=headers, params=parameters)
    
    return response