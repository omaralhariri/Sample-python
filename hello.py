import requests

r = requests.get("http://python.org")
print(r.status_code)
print(r.ok)
