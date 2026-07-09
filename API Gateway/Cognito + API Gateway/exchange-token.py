import requests
import base64

# Define the necessary parameters
client_id = '2kudmph79odp8p4gm55cc94d23'
client_secret = '1qng2qo8ev7n8e5rb7hqvjtfi40bi3vde9sejl3ef4vrj9dralth'
redirect_uri = 'https://patrickphat.fyi'
token_endpoint = 'https://ap-southeast-1pxx8m7pdm.auth.ap-southeast-1.amazoncognito.com//oauth2/token'
authorization_code = '143ba136-85e0-4111-a6b0-4416d58fc034'

# Encode the client ID and client secret
client_credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(client_credentials.encode('utf-8')).decode('utf-8')

# Prepare the request headers and body
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encoded_credentials}'
}

body = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}

# Make the POST request to the token endpoint
response = requests.post(token_endpoint, headers=headers, data=body)

# Check if the request was successful
if response.status_code == 200:
    tokens = response.json()
    id_token = tokens.get('id_token')
    access_token = tokens.get('access_token')
    refresh_token = tokens.get('refresh_token')
    print('ID Token:', id_token)
    print('Access Token:', access_token)
    print('Refresh Token:', refresh_token)
else:
    print('Failed to exchange authorization code for tokens:', response.text)