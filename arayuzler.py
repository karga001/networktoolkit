import  pyfiglet

def giris():
    ascii_art = pyfiglet.figlet_format("Network TOOLKIT")
    print(ascii_art)
    width = len(ascii_art.splitlines()[0])
    text = "v1.0 Made by Karga"
    print(" " * (width - len(text)) + text)

    print("""
    [1] Nmap                    [6] Responder
    [2] Aircrack-ng             [7] Netcat                
    [3] Bettercap               [8] Wireshark
    [4] John The Ripper         [9] Burp Suite
    [5] Hydra              
    Çıkmak için: exit    
    """)

def netcat_arayuz():
    print("""
    [1] Dinleyici Modu (Listen)
    [2] Bağlantı Kur (Connect)
    [3] Dosya Gönder/Al
    """)


def nmaparayuz():
    print("""
        [1] Ağ keşfi (-sn)                              [7] Traceroute (--traceroute)
        [2] Seçilen portu kontrol etme (-p)             [8] TCP/SYN tarama (-sS)
        [3] Tüm portları tarama (-p-)                   [9] Ping taraması (-Pn)
        [4] Servis ve versiyon tespiti (-sV)                
        [5] İşletim sistemi tespiti (-O)                
        [6] Os tespiti, versiyon (agresif tarama -A)
        """)

def aircrackarayuz():
    print("""
    [1] WPA Wordlist Saldırısı
    [2] WEP Kırma
    [3] Handshake Yakalama
    [4] Deauthentication Saldırısı 
    [5] Otomatik WiFi saldırısı
    """)



