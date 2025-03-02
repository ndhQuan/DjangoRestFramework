import requests

endpoint="http://localhost:5000/api/"

res = requests.get(endpoint, json={"query": "123"})

print(res.json())