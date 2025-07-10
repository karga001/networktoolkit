import subprocess
from arayuzler import giris
def bettercap_arayuz():
    print("""
    [1] Ağ koklama (sniffing)
    [2] ARP spoofing
    """)
    secim = input("Seçiminizi yapın: ")
    interface = str(input("Ağ arayüzünüzü girin: "))
    if secim == "1":
        komut = f"sudo bettercap -iface {interface} -caplet http-ui"
    elif secim == "2":
        komut = f"sudo bettercap -iface {interface} -caplet arp.spoof"

    else:
        komut = f"sudo bettercap -iface {interface}"
    subprocess.run(komut, shell=True)