import random
from datetime import datetime

class BankaMusterisi:
    def __init__(self, isim, soyisim, aylik_gelir, pin_kodu):
        self.isim = isim
        self.soyisim = soyisim
        self.hesap_no = random.randint(100000, 999999)
        self.bakiye = 0.0
        self.aylik_gelir = aylik_gelir
        self.kredi_skoru = 1000
        self.pin_kodu = str(pin_kodu)
        self.bloke_durumu = False
        self.kalan_hak = 3

    def log_yaz(self, mesaj):
        su_an = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("banka_loglari.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"[{su_an}] {mesaj}\n")

    def giris_yap(self, girilen_pin):
        if self.bloke_durumu:
            return "BLOKE", "Hesabınız bloke edilmiştir!"
            
        if str(girilen_pin) == self.pin_kodu:
            self.kalan_hak = 3
            self.log_yaz(f"GİRİŞ: {self.isim} {self.soyisim} sisteme girdi.")
            return "BAŞARILI", f"Hoş geldiniz Sayın {self.isim} {self.soyisim}!"
        else:
            self.kalan_hak -= 1
            if self.kalan_hak == 0:
                self.bloke_durumu = True
                self.log_yaz(f"BLOKE: {self.isim} {self.soyisim} hesabı bloke oldu.")
                return "BLOKE", "3 kez hatalı giriş! Hesabınız bloke edildi!"
            return "HATA", f"Yanlış PIN! Kalan hakkınız: {self.kalan_hak}"

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            self.kredi_skoru += 15
            self.log_yaz(f"YATIRMA: {self.isim} hesabına {miktar} TL yatırdı.")
            return f"{miktar} TL başarıyla yatırıldı. Güncel bakiye: {self.bakiye} TL"
            
        return "Geçersiz miktar!"
