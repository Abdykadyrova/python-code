# import requests

# a = requests.get('https://www.tazabek.kg/news:1700965?from=portal&place=last&b=1')
# a = a.text
# file = open("sample.txt", 'a')
# file.write(a)
# print(file)


import requests
d = requests.get('https://ru.sputnik.kg/infographics/20210402/1047892434/orozo-kalendar-post-vremya.html')
d = d.text
file = open('sample.txt','a')
file.write(d)
print(file)