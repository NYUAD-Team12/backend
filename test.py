import requests
data = {
    "username": "admin",
    "project_name": "1234567",
    "project_description": "1234567",
    "project_reward": "1234567",
    "skills": ["beingcool"]
}
base = "http://127.0.0.1:5000/api/project"
res = requests.post(base, json = data)
print(res.json())