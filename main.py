import subprocess
from tools import nmap
from tools import aircrack
from arayuzler import giris
from arayuzler import nmaparayuz
from arayuzler import aircrackarayuz
from tools.aircrack import wpa_crack, wep_crack, capture_handshake, deauth, auto_attack
from tools.bettercap import bettercap_arayuz
from tools.burpsuite import burpsuite_run
from tools.hydra import hydra_attack
from tools.johnripper import john_crack
from tools.responder import responder_baslat
from tools.netcat import netcat_run
from arayuzler import netcat_arayuz
from tools.wireshark import wireshark_run

subprocess.run('sudo apt-get update && apt-get full-upgrade', shell=True)
subprocess.run('sudo apt install -y nmap aircrack-ng bettercap john hydra netcat-openbsd wireshark', shell=True)
subprocess.run('clear', shell=True)

giris()

secim = str(input("Kullanmak istediğin toolu seç: "))

subprocess.run('clear', shell=True)

if secim == "1":
    nmaparayuz()
    nmaps = str(input("istediğiniz parametreyi girin: "))

    if nmaps == "1":
        nmap.kesif()
    elif nmaps == "2":
        nmap.prtkntrl()
    elif nmaps == "3":
        nmap.tumport()
    elif nmaps == "4":
        nmap.servisvryntspt()
    elif nmaps == "5":
        nmap.isltmstm()
    elif nmaps == "6":
        nmap.ostespit()
    elif nmaps == "7":
        nmap.tracer()
    elif nmaps == "8":
        nmap.pngtrmsi()
    elif nmaps == "g":
        subprocess.run('clear', shell=True)
    else:
        print("geçersiz seçim")

elif secim == "2":
    aircrackarayuz()
    secim2 = str(input("İstediğin parametreyi gir: "))
    if secim2 == "1":
        wpa_crack()

    elif secim2 == "2":
        wep_crack()

    elif secim2 == "3":
        capture_handshake()

    elif secim2 == "4":
        deauth()

    elif secim2 == "5":
        auto_attack()

    elif secim2 == "g":
        subprocess.run('clear', shell=True)

elif secim == "3":
    bettercap_arayuz()

elif secim == "4":
    john_crack()

elif secim == "5":
    hydra_attack()

elif secim == "6":
    responder_baslat()

elif secim == "7":
    netcat_arayuz()
    netcat_run()

elif secim == "8":
    wireshark_run()

elif secim == "9":
    burpsuite_run()
