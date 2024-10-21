import os
import subprocess
import sys
import requests
import webbrowser
from pyfiglet import Figlet
from termcolor import colored

# Типа да
required_packages = ['requests', 'pyfiglet', 'termcolor','webbrowser','subprocess']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Заставка
figlet = Figlet(font='slant')
ascii_banner = figlet.renderText("IPCHECKER")
colored_banner = colored(ascii_banner, color='red')
print(colored_banner)

while True:
    ip = input("IP> ")
    if ip.lower() == 'exit':
        break

    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        # Инфа о IP 
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"Хостинг: {data.get('hostname', 'N/A')}")
        print(f"Город: {data.get('city', 'N/A')}")
        print(f"Регион: {data.get('region', 'N/A')}")
        print(f"Страна: {data.get('country', 'N/A')}")
        print(f"Широта, долгота: {data.get('loc', 'N/A')}")
        print(f"Провайдер: {data.get('org', 'N/A')}")

        # Извлечение широты и долготы 
        loc = data.get('loc', '0,0').split(',')
        latitude = loc[0]
        longitude = loc[1]

        # Ссылка на локу
        link = f"https://geotree.ru/coordinates?lat={latitude}&lon={longitude}&z=15&mlat={latitude}&mlon={longitude}&c={longitude},{latitude}"
        print(f"Локация: {link}")

        # Открытие ссылки
        if open_link.lower() == 'да':
            webbrowser.open(link)

    except Exception as e:
        print(f"Ошибка: {e}")
