import json
from pprint import pprint
path = r"C:\Users\aoziso\main\test2.json"
with open(path,"r",encoding="utf-8") as f :
    jsondata = json.load(f)
    pprint(jsondata)
