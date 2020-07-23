import requests as rs
import json


def get(args, url="http://localhost:9200"):
    req = rs.get(url, data=args)
    result = req.json()
    json_result = json.dumps(result, sort_keys=True, indent=4, separators=(', ', ': '))
    return json_result


def post(args, url="http://localhost:9200"):
    req = rs.post(url, data=args)
    result = req.json()
    json_result = json.dumps(result, sort_keys=True, indent=4, separators=(', ', ': '))
    return json_result


def getp(args="", url="http://localhost:9200"):
    result = get(args, url)
    print(result)


def postp(args="", url="http://localhost:9200"):
    result = post(args, url)
    print(result)