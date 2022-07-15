import requests, random, string, threading, os
from pystyle import *

os.system('title github/x8g ^| Github User Checker')
banner = """                                                                           
8 8888      88    d888888o.   8 8888888888   8 888888888o.     d888888o.   
8 8888      88  .`8888:' `88. 8 8888         8 8888    `88.  .`8888:' `88. 
8 8888      88  8.`8888.   Y8 8 8888         8 8888     `88  8.`8888.   Y8 
8 8888      88  `8.`8888.     8 8888         8 8888     ,88  `8.`8888.     
8 8888      88   `8.`8888.    8 888888888888 8 8888.   ,88'   `8.`8888.    
8 8888      88    `8.`8888.   8 8888         8 888888888P'     `8.`8888.   
8 8888      88     `8.`8888.  8 8888         8 8888`8b          `8.`8888.  
` 8888     ,8P 8b   `8.`8888. 8 8888         8 8888 `8b.    8b   `8.`8888. 
  8888   ,d8P  `8b.  ;8.`8888 8 8888         8 8888   `8b.  `8b.  ;8.`8888 
   `Y88888P'    `Y8888P ,88P' 8 888888888888 8 8888     `88. `Y8888P ,88P' """

Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, interval=0.01, time=5)

user = string.ascii_uppercase + string.ascii_lowercase + string.digits
threads = input(Colorate.Horizontal(Colors.blue_to_purple, 'Threads: '))
num = (int(input(Colorate.Horizontal(Colors.blue_to_purple, '3Cs/3Ls | 4Cs/4Ls (3 \ 4): '))))

def check():
    while True:
        userx = ''.join(random.choice(user) for _ in range(num))
        gb = requests.get(f'https://api.github.com/users/{userx}')
        if 'id' in gb.text:
            print(Colorate.Horizontal(Colors.blue_to_white, f'[+] github.com/{userx} | available'))
            with open('avail.txt', 'a') as users:
             users.write(f'github.com/{userx} | https://github.com/x8g\n')
        if 'message' in gb.text:
             print(Colorate.Horizontal(Colors.blue_to_cyan, f'[X] github.com/{userx} | taken'))
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=check).start()
