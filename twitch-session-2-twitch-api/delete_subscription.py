import os
import requests
import json

client_id = os.getenv("TWITCH_CLIENT_ID")
client_secret = os.getenv("TWITCH_CLIENT_SECRET")
broadcaster_user_id = "522799961"
scopes = "user:read:follows"
# for local development you can expose your server with ngrok
callback_url = os.getenv("CALLBACK_URL")

# GET YOUR ACCESS SERVER

response = requests.post(url=
    "https://id.twitch.tv/oauth2/token?"
    f"client_id={client_id}"
    f"&client_secret={client_secret}"
    "&grant_type=client_credentials"
    f"&scope{scopes}"
)

data = json.loads(response.content)
access_token = data.get("access_token")
print(json.dumps(data, sort_keys=True, indent=4))

# DELETE SUBSCRIPTIONS

subscription_ids = [
    "655bd2b3-9325-49c3-9f4c-5578f152ac7e",
    "201e9100-ccb3-41aa-af54-34536f032a27"
]

for subscription_id in subscription_ids:
    response = requests.delete(
        url=f"https://api.twitch.tv/helix/eventsub/subscriptions?id={subscription_id}",
        headers={"Client-ID": client_id, "Authorization": f"Bearer {access_token}", "Content-Type": "application/json"},
    )
    print(response.status_code)