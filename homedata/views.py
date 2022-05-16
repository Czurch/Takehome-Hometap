from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
import requests
import json


def fetchHomeDetails(address, zipcode, field):
    response = requests.get('https://cbca71c7-3204-44f6-8585-f735d28e612e.mock.pstmn.io/getProperty/details?address={addr}&zipcode={zip}'.format(addr = address, zip = zipcode)).json()
    return list(getKeyAtAbritraryDepth(response, field))
    


def propertyData(request, address, zipcode):
    property = fetchHomeDetails(address, zipcode, 'property')
    if not property: return HttpResponseBadRequest('ERROR: 400 - A \'property\' value was not found at external API', status=400)   
    return HttpResponse(json.dumps(property))
    

def getSewer(request, address, zipcode, sewer_type=''):
    sewer = fetchHomeDetails(address, zipcode, 'sewer')
    if sewer is None: return HttpResponseBadRequest('ERROR: 400 - A \'sewer\' value was not found at external API', status=400)   
    if sewer_type == '': return HttpResponse(json.dumps(sewer))
    return HttpResponse(json.dumps(sewer_type in sewer))


#credit to https://stackoverflow.com/questions/9913660/get-value-of-key-in-arbitrary-dictionary-of-unknown-depth
#it should be noted, this returns a generator. This also means that this would return multiple entries if their were fields with the same name
def getKeyAtAbritraryDepth(data, key):
    sub_iter = []
    if isinstance(data, dict):
        if key in data:
            yield data[key]
        sub_iter = data.values()
    if isinstance(data, list):
        sub_iter = data
    for x in sub_iter:
        for y in getKeyAtAbritraryDepth(x, key):
            yield y