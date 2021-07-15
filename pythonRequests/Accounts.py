import json
import requests

url = 'https://api-sandbox.sebgroup.com/ais/v6/identified2/accounts'

#To be adjusted accordingly
bearerToken = 'v3QcwsKxERnwvdyWeEiR'

headers = {
    'Accept': 'application/json',
    'X-Request-ID': '196c556560efdcd704a8b025',
    'PSU-IP-Address': '127.0.0.1',
    'Authorization': 'Bearer ' + bearerToken,
}

response = requests.request("GET", url, headers=headers)
output = json.loads(response.text)
print(json.dumps(output, indent=3, separators=(',', ':'), sort_keys=True))