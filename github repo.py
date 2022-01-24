import webbrowser
user="liad07"
project = input('enter name project  \n')
str = "https://" + user + ".github.io" + project
str1 = "www.github.com/" + user + "/" + project
webbrowser.open(str)
webbrowser.open(str1)
