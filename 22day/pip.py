import termcolor
termcolor.cprint('hello world','cyan','on_yellow',attrs = ['bold'])
print('colored')
text = '{} + {} = {}'.format(10,10,10)
termcolor.cprint(text,'blue',attrs = ['bold'])