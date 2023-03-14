from Credentials import CLIENT_ID, CLIENT_SECRET, URL
import base64, requests, json
from Crawler import Crawler

print("0000")

url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{CLIENT_ID}:{CLIENT_SECRET}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')

print("1111")

headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

print("2222")

r = requests.post(url, headers=headers, data=data)

print("3333")

token = r.json()['access_token']

print("TOKEN: ", token)

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Accept": "application/json",
}

res = requests.get(url=URL, headers=headers)
print(json.dumps(res.json(), indent=2))

