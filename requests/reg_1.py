import requests
api_key = 'fa0c69065a227aae0ae1081d5953bcfa'
site = 'https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric'

city = input('write your city: ')
state = input('write code city: ')
site = site.format(city = city,state = state,api_key = api_key)
date = requests.get(site)
data_dict = date.json()
print('weather in', city)
print("feels_like",data_dict['main']['feels_like'],'градус')
print(data_dict['weather'][0]['main'])
print(data_dict['weather'][0]['description'])
print(data_dict['weather'][1]['preasurre'])


if data_dict['weather'][0]['main']=='Clouds':
    print('погода в',city,'облачно' )

if data_dict['weather'][0]['main']=='Clear':
    print('погода в',city,'ясно' )

