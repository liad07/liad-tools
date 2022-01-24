import webbrowser
steamunlocked="https://steamunlocked.net/?s="
gamestorrents="https://www.gamestorrents.fm/?s="
agfy="https://agfy.co/?s="
game=""
google="https://www.google.com/search?q="
game = input('enter name of game \n')
steamunlocked+=game
gamestorrents+=game
agfy+=game
google+=game

webbrowser.open(steamunlocked)
webbrowser.open(gamestorrents)
webbrowser.open(agfy)
webbrowser.open(google)