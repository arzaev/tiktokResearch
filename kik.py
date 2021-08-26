import requests
import json

url = 'https://clientmetrics-augmentum.kik.com/clientmetrics/augmentum/v1/data?flattened=true'

headers = {
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    'Content-Length': '499',
    'Content-Type': 'application/json',
    'Host': 'clientmetrics-augmentum.kik.com',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Pixel 3 XL Build/PD1A.180720.030)',
    'X-Kik-Augmentum-Api-Token': 'b75de5d51354062e43c7fb23041bf7df567355a6',
    'X-Kik-Augmentum-Api-Token-Index': '1'
}

data = {
    "clientVersion": "15.25.0.22493",
    "commonData:approx_network_type": "wifi",
    "commonData:kik_version": "15.25.0.22493",
    "commonData:model": "Pixel 3 XL",
    "commonData:os_version": "9",
    "commonData:platform": "android",
    "deviceId": "2f10d6db0fda49f9a476f75625a0bf58",
    "devicePrefix": "CAN",
    "event:name": "publicgroupdiscover_hashtag_searched",
    "event:origin": "mobile",
    "eventData:search_term": "age",
    "instanceId": "2c5ca0a7-af61-4b4d-96d4-f890270eee7e",
    "timestamp": "2020-09-08T20:25:21.550Z",
    "userJid": "zirconhenna_x8w",
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.text)