import json

person = {}
login = input('write login: ')
name  =  input('write name: ')

person['login'] = login
person['name'] = name
person_json = open('person.json','w')
json.dump(person,person_json)
print(person)