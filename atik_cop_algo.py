# ATIK ÇÖP ALGORİTMASI   /   AMAÇ : ATIK ÇÖP ATTIKÇA KULLANICIYA PUAN VEREREK BELLİ BİR PUANA GELDİĞİNDE SİNEMA BİLETİ KAZANMASINI SAĞLAMAK.
import sqlite3
class kullanici:
    
    bilgi = open("kullanıcı_bilgi.txt","w")
    print("\nSinematık uygulamasına hoşgeldiniz.\n")
    ad_soyad = input("Ad soyadınızı giriniz : ")
    
    try:
        tc = int(input("T.C kimlik no giriniz : "))
        if len(str(tc)) != 11:
            raise SystemExit("Tc no 11 haneden oluşmalı.İşleminiz iptal edildi...")
    except ValueError:
        raise SystemExit("Tc no sayılardan oluşmalıdır...İşleminiz iptal edildi...")
        
    try:
        sinema_kart = int(input("Sinema kart numaranızı giriniz : "))
        if len(str(sinema_kart)) != 6:
            raise SystemExit("Sinema kart no 6 haneden oluşmalı.İşleminiz iptal edildi...")
    except ValueError:
        raise SystemExit("Sinema kart no sayılardan oluşmalıdır...İşleminiz iptal edildi...")

    print("Ad Soyad : ",ad_soyad, file = bilgi)
    print("T.C Kimlik No : ",tc, file = bilgi)
    print("Sinema Kart No :",sinema_kart, file = bilgi)
    
kullanici1 = kullanici()

atikTurleri = {

    "Kağıt": 1,
    "Plastik": 2,
    "Cam": 3,
    "Metal": 4,
    "Atık Yağ": 5,
    "Atık Pil": 6

}

atıkListesi = list(atikTurleri.items())

#atik = ["Kağıt (1)","Plastik (2)","Cam (3)","Metal (4)","Atık Yağ (5)","Atık Pil (6)"]

fiyat = ["Kağıt = 10 PUAN","Plastik = 25 PUAN","Cam = 10 PUAN","Metal = 100 PUAN","Atık Yağ = 40 PUAN","Atık Pil = 15 PUAN"]

def kağıt1(kağıt):
    return kağıt * 0.1

def plastik1(plastik):
    return plastik * 0.25

def cam1(cam):
    return cam * 0.1

def metal1(metal):
    return metal * 1

def yağ1(yağ):
    return yağ * 0.4

def pil1(pil):
    return pil * 0.15

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
bilet_puanı = 15000

while True:

    bilgi = open("kullanıcı_bilgi.txt","a")

    print("\n100 gram başına puan aşağıdaki gibidir.")
    
    print("\n",fiyat)
    print("\n",atıkListesi)
    
    try:
        atik_secim = int(input("\nHangi atık türünü atacağınızı seçin : "))

        if atik_secim == 1:

            print("Atık kağıt işlemini seçtiniz .")
            kağıt = int(input("Kaç gram atık atacaksınız : "))
            print(kağıt1(kağıt)," puan kazandınız :)")
            p1 = kağıt1(kağıt)
        
        elif atik_secim == 2:

            print("Atık plastik işlemini seçtiniz .")
            plastik = int(input("Kaç gram atık atacaksınız : "))
            print(plastik1(plastik)," puan kazandınız :)")
            p2 = plastik1(plastik)

        elif atik_secim == 3:

            print("Atık cam işlemini seçtiniz .")
            cam = int(input("Kaç gram atık atacaksınız : "))
            print(cam1(cam)," puan kazandınız :)")
            p3 = cam1(cam)

        elif atik_secim == 4:

            print("Atık metal işlemini seçtiniz .")
            metal = int(input("Kaç gram atık atacaksınız : "))
            print(metal1(metal)," puan kazandınız :)")
            p4 = metal1(metal)

        elif atik_secim == 5:

            print("Atık yağ işlemini seçtiniz .")
            yağ = int(input("Kaç gram atık atacaksınız : "))
            print(yağ1(yağ)," puan kazandınız :)")
            p5 = yağ1(yağ)
            
        elif atik_secim == 6:

            print("Atık pil işlemini seçtiniz .")
            pil = int(input("Kaç gram atık atacaksınız : "))
            print(pil1(pil)," puan kazandınız :)")
            p6 = pil1(pil)

        else:
            print("Hatalı işlem ...")

        print("\nToplam Puan : ",p1 + p2 + p3 + p4 + p5 + p6,file = bilgi)

        print("Sinema Bileti Icin Gerekli Puan : ", bilet_puanı - (p1 + p2 + p3 + p4 + p5 + p6),file = bilgi)
        
        print(48*"*",file = bilgi)
        
    except ValueError:
        print("Seçim sadece sayı girişi olmalı...Geçersiz format...")
        

    bilet = p1 + p2 + p3 + p4 + p5 + p6

    if bilet >= 15000:
        print("Tebrikler ! 1 adet sinema bileti kazandınız :)")

    bilgi.close()

    
    devam = int(input("Tamam mı (0) Devam mı (1)"))

    if devam == 0:
        break

    elif devam == 1:
        continue

veritabani = sqlite3.connect("kullanici.db")
baglanti = veritabani.cursor()
baglanti.execute("CREATE TABLE IF NOT EXISTS kullanici(Ad Soyad,Tc,Sinema Kart No)")
sorgu = "insert into kullanici VALUES (?,?,?)"
baglanti.execute(sorgu,(kullanici1.ad_soyad,kullanici1.tc,kullanici1.sinema_kart))

veritabani.commit()
veritabani.close()

print("\nİyi günler dileriz :)\n")
