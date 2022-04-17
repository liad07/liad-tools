import webbrowser
import random
from random import choice
from pytube import YouTube
import keyboard
import pyautogui as auto
import time
import requests
import wikipedia as wiki
from translate import Translator
import subprocess
import speedtest
import socket
import urllib.request


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
    z = ""

    i = 0
    num = input('how much codes you want \n')
    num = (int(num))
    for i in range(num):
        option = ["2480", "2580", "2100", "3060"]
        base = option[random.randint(0, 3)]
        x = (random.randint(0, 5))
        c = (random.randint(0, 5))
        y = (random.randint(0, 5))
        t = (random.randint(0, 5))
        x=str(x)
        c=str(c)
        y=str(y)
        t=str(t)
        print(base+"655"+x+c+y+t+"5")

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
        x = input('enter sentece\n')
        y = input('to which lang convert\n')
        translator = Translator(to_lang=f"{y}")
        translation = translator.translate(f"{x}")
        print(translation)

    def wether():
        x = input('enter a city\n')
        webbrowser.open(f"https://weatherdbi.herokuapp.com/data/weather/{x}")

    def whatsappsend():
        base = "https://api.whatsapp.com/send?text="
        text = input("pleasse enter text to send\n")
        webbrowser.open(base + text)

    def pyqrl():
        from downloads import download
        basic = "https://api.qrserver.com/v1/create-qr-code/?data="

        def wifi():
            wifiname = input("enter name of wifi\n")
            wifipassword = input("enter password of wifi\n")
            download(f"{basic}WIFI:S:{wifiname};T:WPA;P:{wifipassword};;", out_path="qr.png")
            all = f"{basic}WIFI::S:{wifiname};T:WPA;P:{wifipassword};;"
            print(all)

        def mail():
            to = input('To who to send an email\n')
            subject = input('What is the subject of the email\n')
            body = input('What to write in the email\n')
            bl = f"{basic}mailto:{to}?subject={subject}&body={body}"
            download(bl, out_path="qr.png")

        def tel():
            number = input('what the phone\n')
            download(f"{basic}tel:{number}", out_path="qr.png")

        def whatsapp():
            number = input('what the phone\n')
            msg = input('what the message\n')
            download(f"{basic}https://wa.me/972{number}?text{msg}", out_path="qr.png")

        def link():
            link = input('enter a link\n')
            download(f"{basic}{link}", out_path="qr.png")

        def text():
            text = input('enter a text\n')
            download(f"{basic}{text}", out_path="qr.png")
        name2=input("enter a type of qr wifi/mail/tel/whatsapp/link/text\n")
        def pyQRL(name):
            if name == "wifi":
                wifi()
            if name == "mail":
                mail()
            if name == "tel":
                tel()
            if name == "whatsapp":
                whatsapp()
            if name == "link":
                link()
            if name == "text":
                text()
        pyQRL(name2)

    def wikipedia():
        name = input('enter a name\n')
        info = wiki.summary(name)
        print(info)

    def fifateamgen():
        clubs = ["Arsenal", "Aston Villa", "Leicester City", "Chelsea", "Everton", "Manchester City", "Manchester Utd",
                 "Spurs", "Paris SG", "FC Bayern", "Dortmund", "Inter", "juventos", "Roma FC", "Milan", "Lazio",
                 "Soccer Aid", "adidas All-Star", "Barcelona", "Atlético de Madrid", "Real Madrid"]
        NATIONAL = ["Argentina", "Belgium", "Brazil", "England", "France", "Germany", "Italy", "Portugal", "Spain",
                    "Uruguay"]
        all = ['Arsenal', 'Aston Villa', 'Leicester City', 'Chelsea', 'Everton', 'Manchester City', 'Manchester Utd',
               'Spurs', 'Paris SG', 'FC Bayern', 'Dortmund', 'Inter', 'juventos', 'Roma FC', 'Milan', 'Lazio',
               'Soccer Aid', 'adidas All-Star', 'Barcelona', 'Atlético de Madrid', 'Real Madrid', 'Argentina',
               'Belgium', 'Brazil', 'England', 'France', 'Germany', 'Italy', 'Portugal', 'Spain', 'Uruguay']

        def club():
            num = random.randrange(0, len(clubs))
            num2 = random.randrange(0, len(clubs))
            print(clubs[num])
            print(clubs[num2])

        def NATIONAl():
            num1 = random.randrange(0, len(NATIONAL))
            num3 = random.randrange(0, len(NATIONAL))
            print(NATIONAL[num1])
            print(NATIONAL[num3])

        def All():
            num1 = random.randrange(0, len(all))
            num3 = random.randrange(0, len(all))
            print(all[num1])
            print(all[num3])

        x = input("please enter a number 1/2/3 1=club||2=country||3=||shufel\n")
        if x == "1":
            club()
        if x == "2":
            NATIONAl()
        if x == "3":
            All()

    def wifi():
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                'utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))
        input("")

    def speedtestingn():
        wifi = speedtest.Speedtest()
        print("download is:", wifi.download() / 1024 / 1024)
        print("upload is:", wifi.upload() / 1024 / 1024)

    def getip():
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(hostname)
        print(ip)


    print("[1] auto_clicker")
    print("[2] check_web")
    print("[3] gen_password")
    print("[4] google_extension")
    print("[5] iptocountry")
    print("[6] mikud")
    print("[7] translate")
    print("[8] wether")
    print("[9] whatsappsend")
    print("[10] pyQRL")
    print("[11] wikipedia")
    print("[12] fifa team generator")
    print("[13] wifi")
    print("[14] speedtest")
    print("[15] get ip")
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
    if str1 == "10":
        pyqrl()
    if str1 == "11":
        wikipedia()
    if str1 == "12":
        fifateamgen()
    if str1 == "13":
        wifi()
    if str1 == "14":
        speedtestingn()
    if str1 == "15":
        getip()



def github():
    user = "liad07"
    project = input('enter name project  \n')
    str = "https://" + user + ".github.io/" + project
    str1 = "www.github.com/" + user + "/" + project
    webbrowser.open(str)
    webbrowser.open(str1)

def getinformation():
    IP_WEBSITES = ('https://ipinfo.io/ip',
                   'https://ipecho.net/plain',
                   'https://api.ipify.org',
                   'https://ipaddr.site',
                   'https://icanhazip.com',
                   'https://ident.me',
                   'https://curlmyip.net',)

    def getIp():
        for ipWebsite in IP_WEBSITES:
            try:
                response = urllib.request.urlopen(ipWebsite)

                charsets = response.info().get_charsets()
                if len(charsets) == 0 or charsets[0] is None:
                    charset = 'utf-8'  # Use utf-8 by default
                else:
                    charset = charsets[0]

                userIp = response.read().decode(charset).strip()

                return userIp
            except:
                pass  # Network error, just continue on to next website.

        # Either all of the websites are down or returned invalid response
        # (unlikely) or you are disconnected from the internet.
        return None

    loacition = f"https://geolocation-db.com/jsonp/{getIp()}"

    def loc():
        try:
            response = urllib.request.urlopen(loacition)

            charsets = response.info().get_charsets()
            if len(charsets) == 0 or charsets[0] is None:
                charset = 'utf-8'  # Use utf-8 by default
            else:
                charset = charsets[0]

            userIp = response.read().decode(charset).strip()

            return userIp
        except:
            pass  # Network error, just continue on to next website.

    x = loc().replace('"', "")
    y = x.replace("'", "")
    zb = y.replace("callback", "")
    zd = zb.replace("{", "")
    zz = zd.replace("}", "")
    b = zz.replace(")", "")
    c = b.replace("(", "")
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    f = open(f"{hostname}.txt", "a")
    f.write(f"name of owner: {hostname}\nip of network: {ip}\nip of device: {getIp()} \n" + c.replace(',',
                                                                                                      '\n') + "\nwifi name||passwords:\n")
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            f.write("{:<30}|  {:<}".format(i, results[0]) + "\n")

        except IndexError:
            f.write("{:<30}|  {:<}".format(i, "") + "\n")

    f.close()

print("[1] iptvbot")
print("[2] cocacola genrator")
print("[3] downloader_tools")
print("[4] other_tools")
print("[5] github repo")
print("[6] get information\n")
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
if str1 == "6":
    getinformation()

