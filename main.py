from shutil import ExecError
import string
import requests
import os
import threading
from pystyle import Center
from colorama import Fore, init
import random

init()

__lock__ = threading.Lock()
fcl = False
ol = False
tc = 0
lc = 0
hits = 0
takens = 0
fails = 0
tries = 0

def safeprint(str):
    __lock__.acquire()
    print(str)
    __lock__.release()

def check(user):
    try:
        resp = requests.get(f'https://github.com/{user}')
        if resp.status_code == 200:
            return True, resp.status_code
        elif resp.status_code == 404:
            return False, resp.status_code
        else:
            return 'ratelimited', resp.status_code
    except:
        safeprint(Fore.RED + f'     [X] Failed')


banner = """
                          ▄▄ • ▪  ▄▄▄▄▄ ▄ .▄▄• ▄▌▄▄▄▄·      ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
                         ▐█ ▀ ▪██ •██  ██▪▐██▪██▌▐█ ▀█▪    ▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
                         ▄█ ▀█▄▐█· ▐█.▪██▀▐██▌▐█▌▐█▀▀█▄    ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
                         ▐█▄▪▐█▐█▌ ▐█▌·██▌▐▀▐█▄█▌██▄▪▐█    ▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
                         ·▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀▀     ·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀
                                                     yuxontop
                """.replace('.', Fore.RED+'.'+Fore.BLUE).replace('▪', Fore.RED+'▪'+Fore.BLUE).replace('·', Fore.RED+'·'+Fore.BLUE)

def get_random_string(lenght):
    if ol == True:
        return ''.join(random.choice(string.ascii_lowercase) for i in range(lenght))
    else:
        return ''.join(random.choice(string.ascii_lowercase+str(string.digits)) for i in range(lenght))
                    

def update():
    global fails, hits, takens, tries, tc
    while True:
        os.system(f'title GithubUsernameChecker ^| github.com/yuxontop ^| Fails: {fails} ^| Hits: {hits} ^| Taken: {takens} ^| Tries: {tries} ^| Threads: {tc}')


def main():
    global tc, fbl, ol, lc, shit, fip
    os.system('cls')
    print(Center.XCenter(Fore.BLUE + banner))
    print('\n'*4)
    tc = int(input('     [>] How Much Threads You Want ? '))
    fbl = str(input('     [>] From Username List ? (Y/n) ? ')).lower()
    if fbl == 'y':
        fbl = True
        fip = str(input('     [>] Username File Name (leave blank for default) ? '))
        if fip == '':
            fip = 'usernames.txt'
    else:
        fbl = False
        lc = int(input('     [>] Usernames Length ? '))
        ol = str(input('     [>] Do You Want Only Letters In Usernames (Y/n) ? ')).lower()
        if ol == 'y':
            ol = True
        else:
            ol = False
    ut = threading.Thread(target=update)
    ut.start()
    print('\n'*3)
    for thread in range(tc):
        t = threading.Thread(target=Checker)
        t.start()
        

def Checker():
    global tc, fbl, ol, lc, shit, hits, takens, fails, tries, fip
    if fbl:
        with open(fip, 'r+') as f:
            f = f.read().splitlines()
            for username in f:
                try:
                    ia = check(username)
                    tries += 1
                    if ia[0] == False and ia[1] == 404:
                        safeprint(Fore.GREEN + f'     [+] {username} Is Available !')
                        hits += 1
                    elif ia[0] == True and ia[1] == 200:
                        takens += 1
                        safeprint(Fore.RED + f'     [-] {username} Is Taken !')
                except Exception as e:
                    fails += 1
                    safeprint(Fore.RED + f'     [X] Failed')

    else:
        while True:
            username = get_random_string(lc)
            ia = check(username)
            tries += 1
            try:
                if ia[0] == False and ia[1] == 404:
                    safeprint(Fore.GREEN + f'     [+] {username} Is Available !')
                    hits += 1
                elif ia[0] == True and ia[1] == 200:
                    takens += 1
                    safeprint(Fore.RED + f'     [-] {username} Is Taken !')
            except Exception as e:
                fails += 1
                safeprint(Fore.RED + f'     [X] Failed')




    




if __name__ == __name__:
    main()
