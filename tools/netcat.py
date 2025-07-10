import subprocess
from arayuzler import giris
def netcat_run():
    secim = input("İstediğin parametreyi gir: ").strip()

    if secim == "1":
        port = input("Dinlenecek portu girin: ").strip()
        print(f"Dinleyici modda port {port} dinleniyor...")
        komut = f"nc -lvp {port}"
        subprocess.run(komut, shell=True)

    elif secim == "2":
        ip = input("Hedef IP adresini gir: ").strip()
        port = input("Hedef portu gir: ").strip()
        komut = f"nc {ip} {port}"
        subprocess.run(komut, shell=True)

    elif secim == "3":
        mod = input("Dosya gönderilecek mi yoksa alınacak mı? (gonder/al): ").strip().lower()
        port = input("Port numarasını girin: ").strip()

        if mod == "gonder":
            ip = input("Hedef IP adresini gir: ").strip()
            dosya = input("Gönderilecek dosyanın tam yolunu gir: ").strip()
            print(f"{ip} adresine dosya gönderiliyor...")
            komut = f"nc {ip} {port} < {dosya}"
            subprocess.run(komut, shell=True)

        elif mod == "al":
            dosya = input("Kaydedilecek dosya adını gir: ").strip()
            print(f"Port {port} dinleniyor, gelen dosya {dosya} olarak kaydedilecek")
            komut = f"nc -lvp {port} > {dosya}"
            subprocess.run(komut, shell=True)

        else:
            print("geçersiz seçim sadece gonder/al yazabilirsin")

    else:
        print("Geçersiz seçim")
