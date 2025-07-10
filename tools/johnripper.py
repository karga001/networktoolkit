import os
import subprocess

def john_crack():

    hash_file = input("Hash dosyasını girin: ")
    if not os.path.exists(hash_file):
        print("Hash dosyası bulunamadı")
        return

    wordlist = input("Wordlist dosyasını girin: ")
    if not os.path.exists(wordlist):
        print("Wordlist dosyası bulunamadı")
        return

    hedef = str(input("Hedef hash türünü gir (örn: md5crypt, sha512crypt): "))
    komut = f"john --wordlist={wordlist} --format={hedef} {hash_file}"

    print(f"Çalıştırılan komut: {komut}")
    subprocess.run(komut, shell=True, check=True)
    print("Şifre kırma işlemi tamamlandı sonuçları görmek için 'john --show' komutunu kullan")