import json

fjson = open('setting.json')

def getConfig(key):
    dataConfig = json.load(fjson)
    return dataConfig[key]