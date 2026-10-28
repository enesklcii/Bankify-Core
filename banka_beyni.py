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
        self.kart_limiti = aylik_gelir * 2  
        self.kart_borcu = 0.0

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

    def kredi_basvurusu_yap(self, talep_edilen_kredi):
        maksimum_kredi_limiti = self.aylik_gelir * 10
        if self.kredi_skoru < 1100:
            self.log_yaz(f"KREDİ RED: {self.isim} ({self.hesap_no}) - Skor Yetersiz ({self.kredi_skoru}).")
            return False
        # HATA BURADA KESİN OLARAK DÜZELTİLDİ: 'maksimum_kredi_limiti' yapıldı!
        elif talep_edilen_kredi > maksimum_kredi_limiti:
            self.log_yaz(f"KREDİ RED: {self.isim} ({self.hesap_no}) - Gelir Yetersiz.")
            return False
        else:
            self.bakiye += talep_edilen_kredi
            self.kredi_skoru -= 50
            self.log_yaz(f"KREDİ ONAY: {self.isim} ({self.hesap_no}) {talep_edilen_kredi} TL kredi çekti.")
            return True

    def para_gonder(self, alici_musteri, miktar):
        if miktar <= 0:
            return False
        elif self.bakiye < miktar:
            self.log_yaz(f"TRANSFER HATA: {self.isim} yetersiz bakiye nedeniyle {miktar} TL gönderemedi.")
            return False
        else:
            self.bakiye -= miktar
            alici_musteri.bakiye += miktar
            self.log_yaz(f"TRANSFER: {self.isim} ({self.hesap_no}) -> {alici_musteri.isim} ({alici_musteri.hesap_no}) hesabına {miktar} TL yolladı.")
            return True

    def kartla_harca(self, miktar):
        kalan_limit = self.kart_limiti - self.kart_borcu
        if miktar <= 0:
            return "GEÇERSİZ", "Miktar geçersiz!"
        if miktar > kalan_limit:
            return "YETERSİZ", "Kart limiti yetersiz!"
        self.kart_borcu += miktar
        self.kredi_skoru -= 5 
        self.log_yaz(f"KART HARCAMA: {self.isim} kartından {miktar} TL harcadı. Güncel Borç: {self.kart_borcu} TL.")
        return "BAŞARILI", f"{miktar} TL harcama yapıldı."

    def kart_borcu_ode(self, miktar):
        if miktar <= 0:
            return "GEÇERSİZ", "Miktar geçersiz!"
        if miktar > self.bakiye:
            return "YETERSİZ_BAKİYE", "Hesap bakiyeniz yetersiz!"
        if miktar > self.kart_borcu:
            return "FAZLA_MİKTAR", "Borcunuzdan fazlasını ödeyemezsiniz!"
        self.bakiye -= miktar
        self.kart_borcu -= miktar
        self.kredi_skoru += 20 
        self.log_yaz(f"KART ÖDEME: {self.isim} kart borcunun {miktar} TL'sini ödedi.")
        return "BAŞARILI", f"{miktar} TL borç ödendi."
