import webbrowser
import random
def iptv():
    link = "https://liad07.github.io/crack-apps.github.io/assets/iptv/iptv%20project/"
    chanel = input('please enter the chanel \n')
    all = link + chanel
    all = all.lower()
    if chanel == "ספורט1" or chanel == "ספורט 1" or chanel == "51":
        tempch = input('did you mean sport 1 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport1"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)


    elif chanel == "ספורט2" or chanel == "ספורט 2" or chanel == "52":
        tempch = input('did you mean sport 2 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport2"
            all = link + chanel
            all = all.lower()
            webbrowser.open(all)


    elif chanel == "ספורט3" or chanel == "ספורט 3" or chanel == "53":
        tempch = input('did you mean sport 3 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport3"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)


    elif chanel == "ספורט4" or chanel == "ספורט 4" or chanel == "54":
        tempch = input('did you mean sport 4 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport4"
            all = link + chanel
            all = all.lower()
            webbrowser.open(all)

    elif chanel == "ספורט5" or chanel == "ספורט 5" or chanel == "55":
        tempch = input('did you mean sport 5 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport5"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)

    elif chanel == "ספורט5פלוס" or chanel == "ספורט 5 פלוס" or chanel == "56":
        tempch = input('did you mean sport 5 plus ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport5plus"
            all = link + chanel
            all = all.lower()
            webbrowser.open(all)

    elif chanel == "ספורט5גולד" or chanel == "ספורט 5 גולד" or chanel == "57":
        tempch = input('did you mean sport 5 gold ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport5gold"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)

    elif chanel == "ספורט5לייב" or chanel == "ספורט 5 לייב" or chanel == "58":
        tempch = input('did you mean sport 5 live ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "sport5live"
            all = link + chanel
            all = all.lower()
            webbrowser.open(all)


    elif chanel == "כאן11" or chanel == "כאן11" or chanel == "11":
        tempch = input('did you mean kan11  ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "kan11"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)

    elif chanel == "קשת12" or chanel == "קשת 12" or chanel == "12":
        tempch = input('did you mean  keshet12 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "keshet12"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)

    elif chanel == "רשת13" or chanel == "רשת 13" or chanel == "13":
        tempch = input('did you mean reshet13 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "reshet13"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)

    elif chanel == "עכשיו14" or chanel == "עכשיו 14" or chanel == "14":
        tempch = input('did you mean now-14 ? yes/no \n')
        tempch = tempch.lower()
        if tempch == "yes":
            chanel = "now-14"
        all = link + chanel
        all = all.lower()
        webbrowser.open(all)
    else:
        print("the link is not found")
        print("to see optins for bot \nhttps://github.com/liad07/iptv#readme")

def cocacola():
    num = 0
    x = 0
    z = ""
    base = "2480655"
    max = 9999
    min = 1111
    range = max - min + 1
    achdot = 0
    asarot = 0
    meot = 0
    alfim = 0
    i = 0
    num = input('how much codes you want \n')
    num = (int(num))
    while num > i:

        x = (random.randint(1111, 9999))
        if x < 5555 or x < 4555 or x < 3555 or x < 2555 or x < 1555:
            x = str(x)
            base = str(base)
            z = base + x + "5"
            print()
            i += 1
        else:
            achdot = x % 10
            x /= 10
            asarot = x % 10
            x /= 10
            meot = x % 10
            x /= 10
            alfim = x % 10
            x /= 10
            achdot = achdot / 2
            asarot = asarot / 2
            meot = meot / 2
            alfim = alfim / 2
            achdot = round(achdot)
            asarot = round(asarot)
            meot = round(meot)
            alfim = round(alfim)
            achdot = str(achdot)
            asarot = str(asarot)
            meot = str(meot)
            alfim = str(alfim)

            z = base + achdot + asarot + meot + alfim + "5"
            print(int(z))

def font_downloader():
    font = ""
    wfont = ""
    company = ""
    company = input('please enter company aaa/fm \n')
    font = input('please enter font \n')
    wfont = input('please enter weight font \n')
    if company == "aaa":
        webbrowser.open("https://alefalefalef.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-aaa.woff2")
    elif company == "fm":
        webbrowser.open("https://fontimonim.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-fm.woff2")

def github():
    user = "liad07"
    project = input('enter name project  \n')
    str = "https://" + user + ".github.io" + project
    str1 = "www.github.com/" + user + "/" + project
    webbrowser.open(str)
    webbrowser.open(str1)

def games_downloader():
    steamunlocked = "https://steamunlocked.net/?s="
    gamestorrents = "https://www.gamestorrents.fm/?s="
    agfy = "https://agfy.co/?s="
    game = ""
    google = "https://www.google.com/search?q="
    game = input('enter name of game \n')
    steamunlocked += game
    gamestorrents += game
    agfy += game
    google += game

    webbrowser.open(steamunlocked)
    webbrowser.open(gamestorrents)
    webbrowser.open(agfy)
    webbrowser.open(google)
print("[1] iptvbot")
print("[2] cocacola genrator")
print("[3] font_downloader")
print("[4] github repo")
print("[5] games_downloader\n ")
str1 = input('enter num of project project  \n')

if str1=="1":
    iptv()
if str1=="2":
    cocacola()
if str1=="3":
    font_downloader()
if str1=="4":
    github()
if str1=="5":
    games_downloader()