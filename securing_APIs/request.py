import requests
from pprint import pprint

API_URL = "http://localhost:8000"

response = requests.get(
  url=f"{API_URL}/hello",
)

print(response.status_code)
pprint(response.headers)
pprint(response.content)

response = requests.get(
    url=f"{API_URL}/secure",
)

print(response.status_code)
pprint(response.headers)
pprint(response.content)

response = requests.get(
    url=f"{API_URL}/secure",
    headers={
        "access_token": "hello_datascientest"
    }
)

print(response.status_code)
pprint(response.headers)
pprint(response.content)
