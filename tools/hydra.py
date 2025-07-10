import subprocess
import os

def hydra_attack():
    print("\nHedef formatı: ssh://192.168.1.1 veya ftp://192.168.1.1 gibi yaz")
    print("Desteklenen protokoller: ssh, ftp, telnet, smtp, http-post-form, rdp vs\n")

    target = input("Hedefi gir (örn: ssh://192.168.1.1): ").strip()
    if "://" not in target:
        print("Hatalı hedef ssh://192.168.1.1 gibi gir.")
        return

    userlist = input("Kullanıcı listesi dosyasını gir: ").strip()
    if not os.path.exists(userlist):import subprocess

def hydra_attack():
    target = input("hedef (örn: ssh://192.168.0.1): ")
    userlist = input("kullanıcı listesi dosyasını gir: ")
    passlist = input("şifre listesi dosyasını gir: ")
    komut = f"hydra -L {userlist} -P {passlist} {target}"
    subprocess.run(komut, shell=True)
    print("kullanıcı listesi bulunamadı")
    return

    passlist = input("Şifre listesi dosyasını girin: ").strip()
    if not os.path.exists(passlist):
        print("wordlist bulunamadı")
        return

    komut = f"hydra -L {userlist} -P {passlist} {target}"
    print(f"\nÇalıştırılan komut: {komut}\n")

    try:
        subprocess.run(komut, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("hata oluştu tekrar dene")
