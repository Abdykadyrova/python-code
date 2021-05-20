#import os

# cpath = os.getcwd() + '/22day/'
# print(cpath)
# fruicts = [
#     'watermelon\n',
#     'melon\n',
#     'cherryn\n',
#     'banane\n',
#     'cucumber\n',
# ]


# file = open('sample.txt','r') 
# s = file.readlines()
# print(s)

# file = open('sample.txt','a') 
# for f in fruicts:
#     file.write(f +  '\n')


# text = file.readlines()
# print(text)







# akipress = open('https://kg.akipress.org/','r')
# aki_text = akipress.read()
# file = open('sample.txt','w')
# print(akipress.read())






import urllib.request as req
#Читать
link = 'https://www.tazabek.kg/news:1700965?from=portal&place=last&b=1'
akipress = req.urlopen(link)
akipress_text = akipress.read()
print(akipress_text)
file = open('sample.txt','w')
file.write(str(akipress_text))

# import webbrowser
# akipress = webbrowser.open('https://www.tazabek.kg/news:1700965?from=portal&place=last&b=1')
# print(akipress.read())

# webbrowser.register('You tube',None ,webbrowser.BackgroundBrowser('https://www.youtube.com/'))
# webbrowser.get('You tube').open_new_tab('akipress')