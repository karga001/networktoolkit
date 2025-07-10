import subprocess

def kesif():
    ip_range = input("Taramak istediğiniz ağ aralığını girin (örn: 192.168.0.1/24): ")
    subprocess.run(f"nmap -sn {ip_range}", shell=True)

def prtkntrl():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    portlar = input("Taramak istediğiniz portları girin (boşlukla ayırın): ")
    portlar_str = ",".join(portlar.split())

    komut = f"nmap -p {portlar_str} {ip}"
    subprocess.run(komut, shell=True)

def tumport():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = f"nmap -p- {ip}"
    subprocess.run(komut, shell=True)

def servisvryntspt():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = f"nmap -sV {ip}"
    subprocess.run(komut, shell=True)

def isltmstm():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = f"sudo nmap -O {ip}"
    subprocess.run(komut, shell=True)

def ostespit():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = (f"nmap -A {ip}")
    subprocess.run(komut, shell=True)

def tracer():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = (f"sudo nmap --traceroute {ip}")
    subprocess.run(komut, shell=True)

def tcpsyn():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = (f"sudo nmap -sS {ip}")
    subprocess.run(komut, shell=True)

def pngtrmsi():
    ip = input("Taramak istediğiniz IP'yi girin: ")
    komut = (f"nmap -Pn {ip}")
    subprocess.run(komut, shell=True)

