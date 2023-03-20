import requests
import json
import sys

paypal_client_ids = []
with open('list1.txt') as f:
    paypal_client_ids = f.read().splitlines()

live_paypal_clients = []
dead_paypal_clients = []

for client in paypal_client_ids:
    client_id, client_secret = client.split('|')
    url = "https://api.paypal.com/v1/oauth2/token"
    headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
    data = {'grant_type': 'client_credentials'}
    response = requests.post(url, headers=headers, auth=(client_id, client_secret), data=data)
    if response.status_code == 200:
        live_paypal_clients.append(client)
    else:
        dead_paypal_clients.append(client)
    print("{} {}({})".format(client_id, "live" if response.status_code == 200 else "dead", response.status_code))
    
with open('live.txt', 'w') as f:
    for client in live_paypal_clients:
        f.write("{}\n".format(client))
    
with open('dead.txt', 'w') as f:
    for client in dead_paypal_clients:
        f.write("{}\n".format(client))
