import random

class BankMusterisi:
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

# DÜZELTİLEN KISIM: Bu blok artık tamamen sola dayalı, yani fonksiyonun dışında!
if __name__ == "__main__":
    print("==========================================")
    print("== Bankify Core Sistemine Hoş Geldiniz ==")
    print("==========================================")

    # Yeni müşteri oluşturuluyor
    musteri = BankMusterisi("Can", "Öztürk", 40000)
    musteri.bakiye_sorgula()
    
    # 1. Başvuru: Skor 1000 olduğu için RED yiyecek
    musteri.kredi_basvurusu_yap(50000)
    
    # Skor yükseltme işlemleri
    musteri.para_yatir(15000)
    musteri.para_yatir(20000)
    
    # 2. Başvuru: Skor 1030 olduğu için hala RED yiyecek (1100 olması lazım)
    musteri.kredi_basvurusu_yap(120000)
