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
        
        # GÜVENLİK PARAMETRELERİ
        self.pin_kodu = str(pin_kodu)
        self.bloke_durumu = False
        self.kalan_hak = 3

    # KARA KUTU (LOG SİSTEMİ)
    def log_yaz(self, mesaj):
        su_an = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open("banka_loglari.txt", "a", encoding="utf-8") as dosya:
            dosya.write(f"[{su_an}] {mesaj}\n")

    # GÜVENLİK KATMANI (KİMLİK DOĞRULAMA)
    def giris_yap(self, girilen_pin):
        if self.bloke_durumu == True:
            print("[GÜVENLİK UYARISI] Hesabınız bloke edilmiştir! İşlem yapılamaz.")
            return False
            
        if str(girilen_pin) == self.pin_kodu:
            print(f"[BAŞARILI] Giriş onaylandı. Hoş geldiniz, Sayın {self.isim}!")
            self.kalan_hak = 3
            self.log_yaz(f"GİRİŞ BAŞARILI: {self.isim} {self.soyisim} ({self.hesap_no}) sisteme girdi.")
            return True
        else:
            self.kalan_hak -= 1
            print(f"[HATA] Yanlış PIN kodu! Kalan Hakkınız: {self.kalan_hak}")
            if self.kalan_hak == 0:
                self.bloke_durumu = True
                print("[SİBER GÜVENLİK] Hesabınız GÜVENLİK nedeniyle bloke edilmiştir!")
                self.log_yaz(f"HESAP BLOKE: {self.isim} {self.soyisim} ({self.hesap_no}) bloke edildi.")
            return False

    def bakiye_sorgula(self):
        print(f"\n[HESAP BİLGİSİ] Sayın {self.isim} {self.soyisim} -> Bakiyeniz: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"\n[İŞLEM] Hesabınıza {miktar} TL yatırıldı.")
            self.kredi_skoru += 15
            self.log_yaz(f"NAKİT YATIRMA: {self.isim} {self.soyisim} ({self.hesap_no}) hesabına {miktar} TL yatırdı.")
            self.bakiye_sorgula()
        else:
            print(f"\n[HATA] Geçersiz miktar!")

    # ESKİ KOD GERİ GELDİ: KREDİ ALGORİTMASI
    def kredi_basvurusu_yap(self, talep_edilen_kredi):
        print(f"\n[KREDİ BAŞVURUSU] {talep_edilen_kredi} TL için risk değerlendirmesi yapılıyor...")
        maksimum_kredi_limiti = self.aylik_gelir * 10
        
        if self.kredi_skoru < 1100:
            print(f"[RED] Kredi skorunuz yetersiz. (Mevcut: {self.kredi_skoru} / Gereken: 1100+)")
            self.log_yaz(f"KREDİ RED: {self.isim} ({self.hesap_no}) - Skor Yetersiz ({self.kredi_skoru}).")
        elif talep_edilen_kredi > maksimum_kredi_limiti:
            print(f"[RED] Gelir yetersiz. Maksimum limitiniz: {maksimum_kredi_limiti} TL")
            self.log_yaz(f"KREDİ RED: {self.isim} ({self.hesap_no}) - Gelir Yetersiz.")
        else:
            self.bakiye += talep_edilen_kredi
            print(f"[ONAY] Krediniz onaylandı ve hesaba aktarıldı!")
            self.kredi_skoru -= 50
            self.log_yaz(f"KREDİ ONAY: {self.isim} ({self.hesap_no}) {talep_edilen_kredi} TL kredi çekti.")
            self.bakiye_sorgula()

    # ESKİ KOD GERİ GELDİ: HAVALE / EFT SİSTEMİ
    def para_gonder(self, alici_musteri, miktar):
        print(f"\n[TRANSFER] {self.isim} -> {alici_musteri.isim} hesabına {miktar} TL gönderiliyor...")
        if miktar <= 0:
            print("[HATA] Geçersiz miktar!")
        elif self.bakiye < miktar:
            print(f"[RED] Yetersiz Bakiye! Kalan Bakiyeniz: {self.bakiye} TL")
            self.log_yaz(f"TRANSFER HATA: {self.isim} yetersiz bakiye nedeniyle {miktar} TL gönderemedi.")
        else:
            self.bakiye -= miktar
            alici_musteri.bakiye += miktar
            print("[BAŞARILI] Transfer tamamlandı.")
            self.log_yaz(f"TRANSFER: {self.isim} ({self.hesap_no}) -> {alici_musteri.isim} ({alici_musteri.hesap_no}) hesabına {miktar} TL yolladı.")
            self.bakiye_sorgula()


# DEV BİRLEŞİK TEST ALANI
if __name__ == "__main__":
    print("==========================================")
    print("==   BANKIFY CORE FULL SÜRÜM AKTİF      ==")
    print("==========================================")

    # İki müşteri tanımlıyoruz (İsim, Soyisim, Gelir, PIN)
    can = BankaMusterisi("Can", "Öztürk", 45000, "1907")
    merve = BankaMusterisi("Merve", "Yılmaz", 35000, "1234")

    print("\n--- GÜVENLİ GİRİŞ VE SİMÜLASYON BAŞLIYOR ---")
    
    # Can önce yanlış şifre giriyor
    can.giris_yap("0000")
    
    # Can şimdi doğru şifresini girip sisteme sızıyor (Giriş başarılı ise if bloğu çalışır)
    if can.giris_yap("1907"):
        can.para_yatir(25000)          # Para yatırıyor (Skoru artacak)
        can.kredi_basvurusu_yap(80000) # Kredi istiyor (Skor yettiği için onaylanacak!)
        can.para_gonder(merve, 15000)  # Merve'ye para yolluyor
