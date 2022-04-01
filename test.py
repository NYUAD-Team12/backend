import requests
data = {
    "username": "admin"
}
base = "http://127.0.0.1:5000/api/user/project"
res = requests.get(base, json = data)
print(res.json())