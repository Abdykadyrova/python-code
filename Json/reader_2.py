# import json
# file = open('countries.json','w')
# c = []
# while  True:
#     name = input('write name the country or exit: ')
     
#     if name == 'exit':
#         break
#     c.append(name)
# json.dump(c,file)
# # print(file)  




import json
import requests
weather_api_url = 'https://goweather.herokuapp.com/weather/'
city = input('Введите имя города чтобы узнать погоду: ')
req = requests.get(weather_api_url + city)
data = req.json()
print('Погода в ' + city + ': ', end='')
print(data['temperature'])
