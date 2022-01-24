import webbrowser
font=""
wfont=""
company=""
company = input('please enter company aaa/fm \n')
font = input('please enter font \n')
wfont = input('please enter weight font \n')
if company=="aaa":
    webbrowser.open("https://alefalefalef.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-aaa.woff2")
elif company=="fm":
    webbrowser.open("https://fontimonim.co.il/wp-content/fonts/"+font+"/"+font+"-"+wfont+"-fm.woff2")
