import requests
# data = {
#     "username": "nyudemo",
#     "project_name": "job2",
#     "project_description": "jb2",
#     "project_reward": 1267,
#     "skills": {
#         "Handling Saw": 4,
#     } 
# #     }
base = "http://127.0.0.1:5000/api/"
# base2 = "https://resq-api.azurewebsites.net/api/"
# # # res = requests.post(base+'project', json = data)
# # # print(res.json())

# skilll = ['Vehicle Operation', "Nursing", "Reparing", "Cleaning"]
# des = ["Drive", "Clean", "Repair", "Clean"]
# for i  in range(4):
#     skill = {
#         "skill_name": skilll[i],
#         "skill_description": des[i],
#     }
#     res = requests.post(base + 'skill', json = skill)
#     print(res.json())
# res = requests.get(base2 +  'skill')
# print(res.json())

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

res = requests.get(base + 'quantum/sim')
print(res.json())