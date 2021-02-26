import random, string, requests, time
from colorama import Fore
import concurrent.futures
import os
os.system("cls" or "clear")
os.system("title Custom Username Checker V2     By K4Sp3r")
print(Fore.RED+"""

Discord Server :  https://discord.gg/HWdgMvFFdY
        My Discord : @K4Sp3r#1337
   _____ _               _                     ___  
  / ____| |             | |                   |__ \ 
 | |    | |__   ___  ___| | _____ _ __   __   __ ) |
 | |    | '_ \ / _ \/ __| |/ / _ \ '__|  \ \ / // / 
 | |____| | | |  __/ (__|   <  __/ |      \ V // /_ 
  \_____|_| |_|\___|\___|_|\_\___|_|       \_/|____|
                                                    
                                                    
    Made By : K4Sp3r
     Insta : @K4S 
      Snap : Fuun
"""+Fore.WHITE)
time.sleep(.5)
K4 = int(input(Fore.CYAN+"""
        [1] Tiktok
        [2] SoundCloud
        [3] Github
        [4] Twitch
        
        [5] Custom link
        Choose one : """+Fore.WHITE))
webss = ''
webs = ''
if K4 == 1 :
    webss = 'tiktok.com/@'
    webs = "Tiktok"
elif K4 == 2 :
    webss = 'soundcloud.com/'
    webs = "SoundCloud"
elif K4 == 3 :
    webss = 'github.com/'
    webs = "Github"
elif K4 == 4 :
    webss = 'm.twitch.tv/'
    webs = "Twitch"
elif K4 == 5 :
    webss = str(input("Type your link here (without \'https://\') : "))
    webs = webs
else:
    print('Error, please choose correct number.. ')
    time.sleep(3)
    quit()

def check(users): 
    try:
        r = requests.get(f'https://{webss}{users}')
        if r.status_code == 200:
            print(Fore.CYAN+"[-] "+Fore.RED + "UnAvailable"+ Fore.WHITE +' |=>'+Fore.YELLOW+ f' {users}'+Fore.WHITE+" <=|"+Fore.CYAN + " [-]")
        else:
            print(Fore.CYAN + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + ' |=>' + Fore.LIGHTMAGENTA_EX + f' {users}'+Fore.WHITE+" <=|" + Fore.CYAN + " [+]")
            f = open("availables.txt", "a", encoding='utf-8')
            f.write(f"{users} | Available or Banned On => {webs} |\n")
    except:
        pass

with open('usernames.txt', 'r') as f:
    users = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,users)
