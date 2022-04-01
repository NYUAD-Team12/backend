import requests
# data = {
#     "username": "nyudemo",
#     "project_name": "123aa7",
#     "project_description": "12aa37",
#     "project_reward": 1267,
#     "skills": {
#         "Handling Axe": 5,
#     } 
#     }
base = "http://127.0.0.1:5000/api/"
base2 = "https://resq-api.azurewebsites.net/api/"
# res = requests.post(base+'project', json = data)
# print(res.json())
# skill = {
#     "skill_name": "Handling Axe",
#     "skill_description": "Cutting down treese to clear the way. ",
# }
# res = requests.post(base + 'skill', json = skill)
# print(res.json())

# data = {
#     "username": "nyudemo"
# }
# res = requests.get(base + 'user/project', json = data)
# print(res.json())

data = {
    "username": "vol1",
    "email": "vol1@gmail.com",
    "name": "vol1",
    "skills": {"Handling Axe":1}
}
import json
res = requests.post(base + 'vol', json = data)
# res = requests.get(base2 + 'vol')
print(res.json())