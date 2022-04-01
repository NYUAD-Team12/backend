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
    "username": "vol1",
    "email": "vol@gmail.com",
    "name": "vol1",
    "skills": {"beingcool":1}
}
# res = requests.post(base + 'vol', json = data)
res = requests.get(base2 + 'vol')
print(res.json())