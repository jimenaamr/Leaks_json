import commit_leaks
import json

repositorio = './skale/skale-manager'
    
com = commit_leaks.extract(repositorio)
archivo = commit_leaks.transform_and_load(com)

with open('commit_leaks.json','w') as json_file:
    json.dump(archivo, json_file)