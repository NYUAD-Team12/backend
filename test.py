import requests
# data = {
#     "username": "admin",
#     "project_name": "123aa7",
#     "project_description": "12aa37",
#     "project_reward": 1267,
#     "skills": ["beingcool"],
#     "priority": [1]
# }
base = "http://127.0.0.1:5000/api/"
base2 = "https://resq-api.azurewebsites.net/api/"
# res = requests.post(base+'project', json = data)
# print(res.json())
# skill = {
#     "skill_name": "beingcool",
#     "skill_description": "beingcool",
# }
# res = requests.post(base + 'skill', json = skill)
# print(res.json())

# data = {
#     "username": "admin"
# }
# res = requests.get(base + 'user/project', json = data)
# print(res.json())

data = {
    "username": "vol5",
    "email": "vol5@gmail.com",
    "name": "vol5",
    "skills": {"beingcool":1}
}
import json
# res = requests.post(base2 + 'vol', json = data)
res = requests.get(base2 + 'vol')
print(res.json())