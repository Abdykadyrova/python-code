import json
info = {
    "login":"aika",
    "email":"kaokines",
    "age":20,
}
info_json = open('info.json','w')
json.dump(info,info_json)
print(info)
