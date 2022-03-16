import webbrowser
import random
from random import choice
from pytube import YouTube
import keyboard
import pyautogui as auto
import time
import requests


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


def downloader_tools():
    def font_downloader():
        font = ""
        wfont = ""
        company = ""
        company = input('please enter company aaa/fm \n')
        font = input('please enter font \n')
        wfont = input('please enter weight font \n')
        if company == "aaa":
            webbrowser.open(
                "https://alefalefalef.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-aaa.woff2")
        elif company == "fm":
            webbrowser.open(
                "https://fontimonim.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-fm.woff2")

    def game_downloader():
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

    def app_downloader():
        allsoftwares = "https://allsoftwares.co/?s="
        igetintopc = "https://igetintopc.com/?s="
        app = ""
        google = "https://www.google.com/search?q="
        app = input('enter name of app \n')
        igetintopc += app
        allsoftwares += app
        google += app

        webbrowser.open(igetintopc)
        webbrowser.open(allsoftwares)
        webbrowser.open(google)

    def youtube_downloader():
        link = input('enter link\n')
        res = input('enter quality 480/720\n')

        YouTube(f'{link}').streams.filter(progressive=True, file_extension='mp4', res=f"{res}p").first().download()
        print("download is done")
        title = YouTube(f'{link}').title
        print(f"title of video : {title}")
        channel = YouTube(f'{link}').channel_url
        print(f"url of channel : {channel}")
        print(f"url of video: {link}")
        print(f"quality of video: {res}p")
        views = YouTube(f'{link}').views
        print(f"views of video: {views}")
        des = YouTube(f'{link}').description
        print(f"the local link of the video is {title}.mp4")
        print(f"description of video : {des}")

    def media_downloader():
        def movies():
            base = "https://torrentgalaxy.to/torrents.php?search="
            movies = input('please enter name of movie\n')
            webbrowser.open(base + movies + "#results")

        def series():
            # galaxy="https://torrentgalaxy.to/torrents.php?search="
            sdarotv = "https://sdarot.tv/search?term="
            series = input('please enter name of series\n')
            webbrowser.open(sdarotv + series)
            # webbrowser.open(galaxy+series+"#results")

        print("[1] movies")
        print("[2] series\n")
        str1 = input('enter num of  project  \n')
        if str1 == "1":
            movies()
        if str1 == "2":
            series()

    print("[1] font_downloader")
    print("[2] game_downloader")
    print("[3] app_downloader")
    print("[4] youtube_downloader")
    print("[5] media_downloader")
    str1 = input('enter num of  project  \n')
    if str1 == "1":
        font_downloader()
    if str1 == "2":
        game_downloader()
    if str1 == "3":
        app_downloader()
    if str1 == "4":
        youtube_downloader()
    if str1 == "5":
        media_downloader()


def other_tools():
    def auto_clicker():
        while True:
            auto.click()
            if keyboard.is_pressed('space'):
                break

    def check_web():
        url = input('enter url\n')
        time1 = input('Every once in a while you want to check the integrity of the site (Enter number of minutes)\n')
        time1 = int(time1)
        r = requests.get(url)
        x = "liad"
        y = 1
        z = 0
        counter = 0

        while y == 1:
            if r.status_code == 200:
                print("web is online")
            else:
                x = str(r)
                print(r.status_code)
                webbrowser.open("whats mean" + x)
            time.sleep(time1 * 60)
            z = z + 1
            print(f"The site has been checked {z} times")

    def gen_password():
        digits = '0123456789'
        chars = 'abcdefghijklmn' \
                'opqrstuvwxyz'
        up = chars.upper()
        speical = '!@#$%^&*_'
        all = digits + chars + up + speical
        password = ''.join(choice(all) for i in range(8))
        print(password)
        keyboard.wait('space')
        print('enter space to continue')

    def google_extension():
        base = "https://chrome.google.com/webstore/detail/"
        extension_id = input("enter a extension id\n")
        webbrowser.open(base + extension_id)

    def iptocountry():
        x = input('enter ip\n')
        webbrowser.open(f"https://api.ip2country.info/ip?{x}")

    def mikud():
        city = input('enter a city\n')
        street = input('enter a street\n')
        numhouse = input('enter num of the house\n')
        join = input('Enter login\n')
        webbrowser.open(
            f"https://services.israelpost.co.il/zip_data.nsf/SearchZip?OpenAgent&Location={city}&POB=&Street={street}&House={numhouse}&Entrance={join}")
        print(city, street, numhouse, join)

    def translate():
        heb = "https://translate.google.co.il/?hl=iw&sl=iw&tl=en&text="
        eng = "https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text="
        rec = "https://translate.google.co.il/?hl=iw&sl=auto&tl=iw&text="
        var = input('please select type eng/heb/idk \n')

        amen = input('please enter word \n')
        if (var == "heb"):
            webbrowser.open(heb + amen + "&op=translate")
        if (var == "eng"):
            webbrowser.open(eng + amen + "&op=translate")
        if (var == "idk"):
            webbrowser.open(rec + amen + "&op=translate")

    def wether():
        x = input('enter a city\n')
        webbrowser.open(f"https://weatherdbi.herokuapp.com/data/weather/{x}")

    def whatsappsend():
        base = "https://api.whatsapp.com/send?text="
        text = input("pleasse enter text to send\n")
        webbrowser.open(base + text)

    print("[1] auto_clicker")
    print("[2] check_web")
    print("[3] gen_password")
    print("[4] google_extension")
    print("[5] iptocountry")
    print("[6] mikud")
    print("[7] translate")
    print("[8] wether")
    print("[9] whatsappsend")
    str1 = input('enter num of  project  \n')
    if str1 == "1":
        auto_clicker()
    if str1 == "2":
        check_web()
    if str1 == "3":
        gen_password()
    if str1 == "4":
        google_extension()
    if str1 == "5":
        iptocountry()
    if str1 == "6":
        mikud()
    if str1 == "7":
        translate()
    if str1 == "8":
        wether()
    if str1 == "9":
        whatsappsend()


def github():
    user = "liad07"
    project = input('enter name project  \n')
    str = "https://" + user + ".github.io/" + project
    str1 = "www.github.com/" + user + "/" + project
    webbrowser.open(str)
    webbrowser.open(str1)


print("[1] iptvbot")
print("[2] cocacola genrator")
print("[3] downloader_tools")
print("[4] other_tools")
print("[5] github repo\n")
str1 = input('enter num of project project  \n')

if str1 == "1":
    iptv()
if str1 == "2":
    cocacola()
if str1 == "3":
    downloader_tools()
if str1 == "4":
    other_tools()
if str1 == "5":
    github()
