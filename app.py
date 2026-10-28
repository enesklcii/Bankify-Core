import random
# ÖĞRENELİM: Zamanı ve tarihi bilgisayardan çekebilmek için bu kütüphaneyi içeri aktarıyoruz
from datetime import datetime

class BankaMusterisi:
    def __init__(self, isim, soyisim, aylik_gelir):
        self.isim = isim
        self.soyisim = soyisim
        self.hesap_no = random.randint(100000, 999999)
        self.bakiye = 0.0
        self.aylik_gelir = aylik_gelir
        self.kredi_skoru = 1000
    
    # ÖĞRENELİM: İşte bankanın kara kutusu! 
    # Bu fonksiyon her çağrıldığında, aldığı mesajı otomatik olarak 'banka_loglari.txt' dosyasına yazar.
    def log_yaz(self, mesaj):
        # Bilgisayarın şu anki tarih ve saatini şık bir formatta (Gün-Ay-Yıl Saat:Dakika:Saniye) alıyoruz
        su_an = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        # 'banka_loglari.txt' dosyasını "append (ekleme)" modunda açıyoruz.
        # encoding="utf-8" yazıyoruz ki Türkçe karakterler (ş, ı, ğ) bozulmasın.
        with open("banka_loglari.txt", "a", encoding="utf-8") as dosya:
            # Dosyaya zaman damgasıyla birlikte mesajı yaz ve \n ile bir alt satıra geç
            dosya.write(f"[{su_an}] {mesaj}\n")

    def bakiye_sorgula(self):
        print(f"\n[HESAP BİLGİSİ] Sayın {self.isim} {self.soyisim} ({self.hesap_no}) -> Güncel Bakiyeniz: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"\n[İŞLEM] Hesabınıza {miktar} TL yatırıldı.")
            self.kredi_skoru += 15
            
            # ÖĞRENELİM: İşlem başarılı olduğu için log dosyasına bilgi gönderiyoruz
            self.log_yaz(f"HESAP NO {self.hesap_no}: {self.isim} {self.soyisim} hesabına {miktar} TL nakit yatırdı. Yeni Bakiye: {self.bakiye} TL.")
            
            self.bakiye_sorgula()
        else:
            print(f"\n[HATA] Geçersiz para miktarı girdiniz.")

    def kredi_basvurusu_yap(self, talep_edilen_kredi):
        print(f"\n[KREDİ BAŞVURUSU] {talep_edilen_kredi} TL için değerlendirme başlatıldı...")
        maksimum_kredi_limiti = self.aylik_gelir * 10
        
        if self.kredi_skoru < 1100:
            print(f"[RED] Kredi skorunuz yetersiz.")
            # ÖĞRENELİM: Banka güvenliği için reddedilen krediyi logluyoruz
            self.log_yaz(f"KREDİ RED: {self.isim} {self.soyisim} ({self.hesap_no}), {talep_edilen_kredi} TL kredi talep etti. SEBEP: Yetersiz Kredi Skoru ({self.kredi_skoru}).")
        
        elif talep_edilen_kredi > maksimum_kredi_limiti:
            print(f"[RED] Gelir yetersiz.")
            self.log_yaz(f"KREDİ RED: {self.isim} {self.soyisim} ({self.hesap_no}), {talep_edilen_kredi} TL kredi talep etti. SEBEP: Limit Aşımı (Maksimum Limit: {maksimum_kredi_limiti}).")
        
        else:
            self.bakiye += talep_edilen_kredi
            print(f"[ONAY] Tebrikler, krediniz onaylandı ve bakiyeniz hesabınıza aktarıldı.")
            self.kredi_skoru -= 50
            
            # ÖĞRENELİM: Onaylanan büyük parayı hemen rapora yazıyoruz
            self.log_yaz(f"KREDİ ONAY: {self.isim} {self.soyisim} ({self.hesap_no}) hesabına {talep_edilen_kredi} TL kredi tanımlandı.")
            
            self.bakiye_sorgula()

    def para_gonder(self, alici_musteri, miktar):
        print(f"\n[TRANSFER] {self.isim} {self.soyisim} -> {alici_musteri.isim} {alici_musteri.soyisim} hesabına {miktar} TL gönderiliyor...")
        
        if miktar <= 0:
            print("[HATA] Geçersiz transfer miktarı!")
        elif self.bakiye < miktar:
            print(f"[RED] Yetersiz Bakiye! Transfer gerçekleştirilemedi.")
            # ÖĞRENELİM: Başarısız para gönderme denemesini sisteme kaydediyoruz
            self.log_yaz(f"TRANSFER HATA: {self.isim} -> {alici_musteri.isim} hesabına {miktar} TL göndermek istedi ama bakiyesi yetersizdi.")
        else:
            self.bakiye -= miktar
            alici_musteri.bakiye += miktar
            print("[BAŞARILI] Para transferi güvenle tamamlandı.")
            
            # ÖĞRENELİM: En kritik log; para bir hesaptan çıktı, diğerine girdi!
            self.log_yaz(f"TRANSFER: {self.isim} ({self.hesap_no}) kullanıcısı, {alici_musteri.isim} ({alici_musteri.hesap_no}) kullanıcısına {miktar} TL transfer etti.")
            
            self.bakiye_sorgula()
            alici_musteri.bakiye_sorgula()


# Test Alanı
if __name__ == "__main__":
    print("==========================================")
    print("== Bankify Core Sistemine Hoş Geldiniz ==")
    print("==========================================")

    # Müşterileri oluştur
    can = BankaMusterisi("Can", "Öztürk", 40000)
    merve = BankaMusterisi("Merve", "Yılmaz", 30000)
    
    # Finansal hareketleri simüle et
    can.para_yatir(5000)
    can.kredi_basvurusu_yap(80000) # Skor 1015 olduğu için RED yiyecek
    can.para_gonder(merve, 2000)  # Başarılı transfer
    can.para_gonder(merve, 4000)  # Yetersiz bakiye hatası
