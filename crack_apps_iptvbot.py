import webbrowser


link="https://liad07.github.io/crack-apps.github.io/assets/iptv/iptv%20project/"
chanel= input ('please enter the chanel \n')
all=link+chanel
all=all.lower()
if chanel== "ספורט1" or chanel=="ספורט 1" or chanel=="51":
    tempch = input('did you mean sport 1 ? yes/no \n')
    tempch=tempch.lower()
    if tempch=="yes":
     chanel="sport1"
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
# elif chanel=="now-14" or chanel=="reshet13" or chanel=="keshet12" or chanel=="kan11":
#     print("news category")
# elif chanel == "sport1" or chanel == "sport2" or chanel == "sport3" or chanel == "sport4" or chanel == "sport5" or chanel == "sport5live" or chanel == "sport5plus" or chanel == "sport5gold":
#     print("sport category")
