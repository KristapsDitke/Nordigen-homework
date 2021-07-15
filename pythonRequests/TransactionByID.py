import json
import requests

url = 'https://api-sandbox.sebgroup.com/ais/v7/identified2/accounts/5a59028c-e757-4f22-b88c-3ba90573383c/transactions/6f24de7e-9f81-4f09-999a-b33bead16e8d'

#To be adjusted accordingly
bearerToken = 'EpVzykSlffqh0tCn0q4C'

headers = {
    'Accept': 'application/json',
    'X-Request-ID': '196c556560efdcd704a8b025',
    'PSU-IP-Address': '127.0.0.1',
    'Authorization': 'Bearer ' + bearerToken,
}

response = requests.request("GET", url, headers=headers)
output = json.loads(response.text)
print(json.dumps(output, indent=3, separators=(',', ':'), sort_keys=True))