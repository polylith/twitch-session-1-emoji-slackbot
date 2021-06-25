import requests
import os

response = requests.post(url=os.getenv("CALLBACK_URL"), json={"subscriber": "Daniel", "challenge": "1234"})
print(response.content)