import subprocess
import os
from arayuzler import giris

def responder_baslat():
    kur = str(input("responder kurulu mu? E/H:"))
    if kur == "e":
        interface = input("Ağ arayüzünü gir (örn: eth0, wlan0): ").strip()

        if not interface:
            print("Ağ arayüzü boş olamaz")
            return

        responder_yolu = "/usr/share/responder/Responder.py"

        komut = f"sudo python3 {responder_yolu} -I {interface}"
        print(f"\nÇalıştırılan komut: {komut}\n")

        try:
            subprocess.run(komut, shell=True)
        except subprocess.CalledProcessError:
            print("hata oluştu tekrar dene")

    else:
        print("responder'ı kur")