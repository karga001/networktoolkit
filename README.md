# Karga Hardening Script

Bu script kurumsal (enterprise) tehdit modellerini hedeflemez; Debian 13 stable üzerinde günlük kullanım için optimize edilmiştir.

## 1) Bu script ne iş yapıyor?

Bu script sistemi gereksiz şişirmeden, boş laf üretmeden net şekilde sıkılaştırır.

Amaç: saldırganın işini zorlaştırmak, açık kapıları kapatmak, zayıf noktaları minimuma indirmek.

Script şunları yapar:

- Ağ, DNS, firewall, USB, sandbox ve çekirdek tarafında katı kurallar uygular
- Sistem servislerini, izinlerini ve kernel parametrelerini daha güvenli hâle getirir
- Gereksiz servisleri kapatır, gereksiz riskleri temizler
- Tarayıcıyı ve uygulamaları firejail + apparmor ile ayrı kafeslere alır
- MAC, DNS, network fingerprinting gibi iz bırakabilecek noktaları törpüler
- Exploit geldiğinde zararın yayılmasını sınırlar
- Saldırı yüzeyini küçültür, gereksiz açık kapıları kapatır
- Günlük kullanımda fark edilmeyen ama kritik olan zayıflıkları otomatik kapatır

Özet: Bu script saldırıyı imkânsız yapmaz; uğraştırır, zaman kaybettirir, bazı noktalarda saf dışı bırakır.

## 3) Kime karşı etkili?

Bu script bir anda “devlet seviyesi koruma” vermez ama günlük hayatta karşılaşacağın saldırganların %90’ını boğar.

Durdurduğu profil:

- Hazır exploit arayan, tool çalıştırıp şans deneyen, nmap/naabu/nessus tarayıp açık kovalayanlar
- IPv4’ü süpüren, zayıf port arayan, exploit paketleyen otomatik botlar
- Lokal exploit deneyen, browser’dan içeri girmeye çalışan, USB’den payload sokmaya uğraşanlar
- Discord’dan topladığı exploit’lerle sisteme girmeye çalışanlar
- MAC/DNS üzerinden iz sürmeye çalışan yarım yamalak saldırganlar
- Kernel hardening’i geçemeyen, privilege escalation kovalayan, network pivot denemek isteyen insanlar
- Yan servislerden dolanıp içeri yürümeyi hedefleyen çakallar
- Ağ üzerinden “ufak tefek paket oyunları” ile içeri sızacağını düşünenler

Bu düzeydeki herkesin önünü keser.

## 4) Engelleyebildiği/zorlaştırdığı saldırılar

Scriptin tam olarak kestiği veya ciddi şekilde zorlaştırdığı şeyler:

- Tarayıcı istismarından sonra sistem içine yayılma girişimleri
- MAC, DNS, fingerprinting ile kimlik izi çıkarma denemeleri
- BadUSB, HID injection, sahte klavye/mouse gibi USB saldırıları
- Dışarıdan port tarama, servis tespiti, açık servis bulma çabaları
- Yan servisler üzerinden içeri dolanma senaryoları
- Temel ağ tabanlı saldırılar, düşük seviye paket manipülasyonları
- Kernel parametreleri üzerinden yapılabilecek bazı zorlama yöntemleri
- Firejail/AppArmor bypass denemelerinin büyük kısmı

Kısaca ortalama saldırgan bu sisteme dokunamaz.

## 5) Kimler hâlâ sızabilir?

Bu script güçlü, evet.

Ama fiziksel kuralları, insan kaynaklı salaklık düzeyi (sosyal mühendislik ve bilinmeyen içeriğe yetki verme) ve 0‑day piyasasını yenemez.

Bu hardening ile içeri giremeyenler:

- Script‑kiddie çöplüğü
- Discord/YouTube hırdavatçıları
- Otomatik botlar
- Kopyala‑yapıştır exploitçiler
- “Port taradım açık yok mu”
- USB/Payload denemecileri
- Tarayıcı exploit’inden shell bekleyenler
- Ele geçirme umuduyla mass‑scan yapan kitle

Bu hardening ile zorlananlar:

- Deneyimli bireysel saldırganlar
- Linux privilege‑escalation uzmanları
- Network pivot ve yan servis kovalayanlar

Bu hardening’i aşabilecek tek grup:

- APT düzeyi, özel exploit geliştiren gerçek profesyoneller
- Fiziksel erişimi olan ekipler

Bu script bu seviyeye karşı “tam koruma” iddiasında olmaz — kimse olamaz.

Ama saldırı yüzeyini daraltır, açıklarını azaltır, eşiği yükseltir.

## 7) Hangi araçları kullanıyor?

Bu script sistemde zaten bulunan mekanizmaları sonuna kadar kullanıyor, dışarıdan çöplük taşımıyor.

Kullanılan araçlar:

- UFW → basit ama etkili firewall
- AppArmor → çekirdek seviyesinde confinement
- Firejail → uygulama sandbox’ı
- USBGuard → USB saldırılarına karşı kontrol katmanı
- macchanger → MAC rastgeleleştirme
- TLP → pil/enerji optimizasyonu
- Powertop → derin enerji ayarı
- sysctl → ağ, kernel ve hafıza tarafında sıkı parametreler
- systemd → gereksiz servis kapatma / temizleme
- dns ayarları → güvenli resolver, sızıntı engelleme

## 8) Script tam olarak ne yapıyor?

- MAC adreslerini rastgeleleştirir  
- DNS’i güvenli moda çeker  
- UFW firewall’ı kapı duvarına çevirir  
- AppArmor’u aktif eder  
- Firejail sandbox uygular  
- USBGuard ile USB cihazlarını kontrol eder  
- Kernel ve sysctl parametrelerini sertleştirir  
- Gereksiz servisler kapatılır  
- Pil ve güç ayarları optimize edilir  
- Disk erişim parametreleri sıkılaştırılır  
- /tmp, /var/tmp, /dev/shm noexec/nosuid yapılır  
- Önemli dosyalara izin sıkılaştırması uygulanır  

## Kullanım

# Kurulum

```bash
git clone https://github.com/karga001/karga-master-hardening.git
cd karga-master-hardening/
chmod +x karga-master-hardening.sh
sudo ./karga-master-hardening.sh
```

# Kalıcı yapmak için:
```bash
sudo nano /etc/systemd/system/hardening.service
```
# İçine yapıştır:
```bash
[Unit]
Description=Karga Hardening
After=network.target local-fs.target
Wants=network.target

[Service]
Type=oneshot
ExecStart=/home/KULLANICIADI/karga-master-hardening/karga-master_hardening.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

# Aktifleştirme:
```bash
systemctl daemon-reload
systemctl enable hardening.service
systemctl start hardening.service
```




