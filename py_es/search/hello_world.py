from py_es.util import json_util
import requests

req = requests.get("http://localhost:9200")
result = req.json()
json_result = json_util.format_json(result)
print(json_result)
