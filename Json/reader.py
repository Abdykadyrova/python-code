import json


user = {
    "name":"NUrbek",
    "age":23,       
    "birthDate":"12.12.2001",
    "city" : "osh"
}


users_json = open('users.json','w')
# user_json_r = users_json.read

json.dump(user,users_json)

users_json = open('user.json','r')
user_dict = json.load(user_json)
print(user_dict)

# user_dict = json.load(users_json)
# print(user_dict['name'])