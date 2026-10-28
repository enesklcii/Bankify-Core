import random

class BankaMusterisi:
    def __init__(self, isim, soyisim, aylik_gelir):
        self.isim = isim
        self.soyisim = soyisim
        self.hesap_no = random.randint(100000, 999999)
        self.bakiye = 0.0
        self.aylik_gelir = aylik_gelir
        self.kredi_skoru = 1000
    
    def bakiye_sorgula(self):
        print(f"\n[HESAP BİLGİSİ] Sayın {self.isim} {self.soyisim} ({self.hesap_no}) -> Güncel Bakiyeniz: {self.bakiye} TL")

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"\n[İŞLEM] Hesabınıza {miktar} TL yatırıldı.")
            self.kredi_skoru += 15
            self.bakiye_sorgula()
        else:
            print(f"\n[HATA] Geçersiz para miktarı girdiniz.")
    
    def kredi_basvurusu_yap(self, talep_edilen_kredi):
        print(f"\n[KREDİ BAŞVURUSU] {talep_edilen_kredi} TL için değerlendirme başlatıldı...")
        maksimum_kredi_limiti = self.aylik_gelir * 10
        
        if self.kredi_skoru < 1100:
            print(f"[RED] Kredi skorunuz yetersiz.")
            print(f"-> Mevcut Kredi Skorunuz: {self.kredi_skoru} (Gereken: 1100+)")
        elif talep_edilen_kredi > maksimum_kredi_limiti:
            print(f"[RED] Gelir yetersiz.")
            print(f"-> Maksimum alınabilecek kredi: {maksimum_kredi_limiti} TL'dir.")
        else:
            self.bakiye += talep_edilen_kredi
            print(f"[ONAY] Tebrikler, krediniz onaylandı ve bakiyeniz hesabınıza aktarıldı.")
            self.kredi_skoru -= 50
            self.bakiye_sorgula()

    # YENİ ÖZELLİK: Havale / EFT (Para Transferi) Fonksiyonu
    def para_gonder(self, alici_musteri, miktar):
        print(f"\n[TRANSFER] {self.isim} {self.soyisim} -> {alici_musteri.isim} {alici_musteri.soyisim} hesabına {miktar} TL gönderiliyor...")
        
        # Kontrol 1: Gönderilmek istenen miktar sıfırdan büyük mü?
        if miktar <= 0:
            print("[HATA] Geçersiz transfer miktarı!")
            
        # Kontrol 2: Gönderen kişinin hesabında o kadar para var mı?
        elif self.bakiye < miktar:
            print(f"[RED] Yetersiz Bakiye! Transfer gerçekleştirilemedi.")
            print(f"-> Eksik Miktar: {miktar - self.bakiye} TL")
            
        # Şartlar tamam ise transferi yap
        else:
            self.bakiye -= miktar            # Parayı gönderenin bakiyesinden düş
            alici_musteri.bakiye += miktar    # Parayı alıcının bakiyesine ekle
            print("[BAŞARILI] Para transferi güvenle tamamlandı.")
            
            # İşlem sonrası iki tarafın da son durumunu ekrana yazdır
            self.bakiye_sorgula()
            alici_musteri.bakiye_sorgula()


# Yeni Test Alanı
if __name__ == "__main__":
    print("==========================================")
    print("== Bankify Core Sistemine Hoş Geldiniz ==")
    print("==========================================")

    # 1. Simülasyon için iki farklı müşteri oluşturuyoruz
    gonderen = BankaMusterisi("Can", "Öztürk", 40000)
    alici = BankaMusterisi("Merve", "Yılmaz", 30000)
    
    # 2. Can hesabına başlangıç parası yatırıyor
    gonderen.para_yatir(5000)
    
    # 3. Can, Merve'ye 2000 TL transfer ediyor (Başarılı olması lazım)
    gonderen.para_gonder(alici, 2000)
    
    # 4. Can, Merve'ye bir kez daha 4000 TL göndermeyi deniyor (Bakiyesi yetmediği için RED yiyecek)
    gonderen.para_gonder(alici, 4000)
