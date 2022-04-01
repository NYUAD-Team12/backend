import requests
# data = {
#     "username": "nyudemo",
#     "project_name": "job2",
#     "project_description": "jb2",
#     "project_reward": 1267,
#     "skills": {
#         "Handling Saw": 4,
#     } 
#     }
base = "http://127.0.0.1:5000/api/"
base2 = "https://resq-api.azurewebsites.net/api/"
# res = requests.post(base+'project', json = data)
# print(res.json())
skill = {
    "skill_name": "Handling Sawaa",
    "skill_description": "Cutting down treese to clear the way. ",
}
res = requests.post(base2 + 'skill', json = skill)
print(res.json())

# # data = {
# #     "username": "nyudemo"
# # }
# # res = requests.get(base + 'user/project', json = data)
# # print(res.json())

# data = {
#     "username": "vol2",
#     "email": "vol2@gmail.com",
#     "name": "vol2",
#     "skills": {"handling Saw":5,"Handling Axe":1}
# }
# res = requests.post(base + 'vol', json = data)
# res = requests.get(base + 'vol')
# print(res.json())

# res = requests.get(base2 + 'quantum/sim')
# print(res.json())