import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'

data = { 'name': 'DevOps Journey', 
         'Channel URL': 'https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg' }

print("Sending...")
r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print("Sent and receive status code: " + str(r.status_code) + ".")
