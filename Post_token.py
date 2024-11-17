import os, sys
os.system("clear")
os.system('pip uninstall requests -y')
os.system('pip install requests')
os.system('pip install --upgrade urllib3')
import requests
import json
import time
import sys
from platform import system
import os
import subprocess
import http.server
import socketserver
import threading
import getpass
from colorama import Fore, Style
from datetime import datetime
from time import sleep
from os import system as sh
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
def approval():
  os.system('git pull')
  time.sleep(1)
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = "SID-"+"".join(uuid)
  os.system('clear')
  print("\033[1;37m [\u001b[36\033[1;37m] You Need Approval To Use This Tool   \033[1;37m")
  print("\033[1;37m [\u001b[36\033[1;37m] Your Key :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m----------------------------------------------""")
  try:
    httpCaht = requests.get("https://pastebin.com/raw/zjBiVcNj").text
    if id in httpCaht:
      print("\033[1;97m >> Your Key Has Been Approved !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      print("\x1b[1;97m >> Sorry Your Key Has Not Been Approved ");
      time.sleep(0.1)
      input('IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+919724919806?text='+tks),approval()
      time.sleep(1)
      exit()
  except Exception as e:
     print(e)
     print(" >> Unable To Fetch Data From Server ")
     time.sleep(2)
     exit()
approval()


logo = r'''

 ___________________________________________
                        

____ ___ ____      __  ______  
/ ___|_ _|  _ \     \ \/ |  _ \ 
\___ \| || | | |_____\  /| | | |
 ___) | || |_| |_____/  \| |_| |
|____|___|____/     /_/\_|____/ 
                                        
____________________________________________

[ ᴘᴏꜱᴛ ʟᴏᴀᴅᴇʀ ᴛᴏᴏʟꜱ ᴡɪᴛʜ ᴛᴏᴋᴇɴ ]

[ ᴛʜɪꜱ ᴛᴏᴏʟꜱ ɪꜱ ᴍᴀᴅᴇ ʙʏ {{. ꜱɪᴅ  }} ]

[ ᴡʜᴀᴛꜱᴀᴘᴘ ɴᴜᴍʙᴇʀ ---|| 9724919806 || ] 
____________________________________________        
'''
# Print the logo
print(Fore.CYAN + logo +  Style.RESET_ALL)

 # Prompt Password 
def pas():
    print('\u001b[37m' + '---------------------------------------------------')
    password = input("Password : ") 
    print('--------------------------------------------')
    mmm = requests.get('https://pastebin.com/raw/nndPaBpD').text

    if mmm not in password:
        print('[-] <==> Incorrect Password!')
        sys.exit()
        
pas()

def send_messages():
    token_file = input(f"Enter the Token File : ") 
    tokens = open(token_file,"r").read().splitlines()
    num_tokens = len(tokens)

    requests.packages.urllib3.disable_warnings()

    def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
    cls()

    def liness():
        print('\33[0;37;40m---------------------------------------------------')

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }

    liness()

    access_tokens = [token.strip() for token in tokens]

    
    convo_id = input(f"Enter the Post ID : ")

    
    text_file_path = input(f"Enter the Messages File : ") 

    
    messages = open(text_file_path,"r").readlines()

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    
    haters_name = input(f"Enter Hater Name : ")

    
    speed = int(input(f"Enter Delay : ")) 

    liness()

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v15.0/{}/comments".format(convo_id)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("[+] Comment {} of Post {} sent by Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                else:
                    print("[x] Failed to send Comment {} of Post {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                    print("  - Time: {}".format(current_time))
                    liness()
                    liness()
                time.sleep(speed)

            print("[+] All messages sent. Restarting the process...")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    send_messages()
    pas()

if __name__ == '__main__':
    main()
