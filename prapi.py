import requests
import json

re = requests.get("https://reqres.in/api/users?page=2")
res = re.json()
print(res)
"""for i in res["data"]:
    print(i)
    if i["id"]==11:
        print(i['first_name'])"""

for i in res["data"]:
    for j in i:
        if j == "id":
            print(i[j])