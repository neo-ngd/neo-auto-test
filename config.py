import json

config = {}
with open('config.json', 'r') as configfile:
    res = json.load(configfile)
    config['neoclipath'] = res['neoclipath']