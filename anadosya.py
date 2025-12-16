import time
import config

print("daha bitmedi")
def oyun():
   print("dont forgot to edit here")
   time.sleep(2)
   oyun()
       
      
def sifresifirlamakullanici():
     cevapsifresifirla = input("sifrenizi sifirlamak icin once kurtarma kodunuzu giriniz, yoksa x i girin: ")
     if cevapsifresifirla == config.kurtarmakodu:
         cevapsifresifirla2 = input("Kurtarma sorusunu giriniz (soru yok sadece cevap ornegin armut): ")
         if cevapsifresifirla2 == config.kurtarmasoru:
             yeni_sifrekullanicigir = input("Yeni sifrenizi giriniz: ")
             config.kayitlikullanicisifre = yeni_sifrekullanicigir
             print("Sifreniz basariyla degistirildi.")
             time.sleep(1)
             anadosya()
         else:
            print("Kurtarma sorusu yanlis.")
            print("Girise gidiyonuz.")
            time.sleep(1)
            anadosya()
def yanlisifresifre():
    if config.denemehakki == 0:
        print("zaman aşimi. Yanliş şifrei,", config.uyu, "saniye bekleyin.")
        time.sleep(config.uyu)
        config.denemehakki = config.denemehakkirefresh
        anadosya() # sure dolunca girise atcak
def yanlisifisim():
    if config.isimdeneme == 0:
        print("zaman aşimi. Yanliş isim,", config.uyu, "saniye bekleyin.")
        time.sleep(config.uyu)
        config.isimdeneme = config.denemehakkirefresh
        anadosya()

def sifregiris():
    sifresor = input("Sifrenizi giriniz: ")
    if sifresor == config.kayitlikullanicisifre:
        print("Giris basarili.")
        oyun()
    else:
        config.denemehakki -= 1
    print("Yanlis sifre. Kalan deneme hakkiniz:", config.denemehakki)
    if config.denemehakki == 0:
            yanlisifresifre()
    if config.denemehakki == 1:
        time.sleep(0.3)
        sorusorcikkalsifre = input("Son denemeniz. Devam etmek için 1, cikmak icin 2, sifre kurtarma icin 3'e basiniz: ")
        time.sleep(1)
        if sorusorcikkalsifre == "1":
            sifregiris()
        elif sorusorcikkalsifre == "2": 
                exit("cikis yapildi")
        elif sorusorcikkalsifre == "3":
             sifresifirlamakullanici()
                       
    sifregiris()

        
def anadosya():
    isimsor = input("Isminizi giriniz: ")
    if isimsor == config.kayitlikullaniciadi:
        sifregiris()
    else:
        config.isimdeneme -= 1
        print("Yanlis isim. Kalan deneme hakkiniz:", config.isimdeneme)
        if config.isimdeneme == 0:
            yanlisifisim()
        if config.isimdeneme == 1:
            print("Son denemeniz.")
        anadosya()

anadosya()
    