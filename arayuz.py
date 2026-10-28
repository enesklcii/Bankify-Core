import tkinter as tk
from tkinter import messagebox
# ÖĞRENELİM: Yan sayfadaki banka mantığını bu görsel sayfaya ithal ediyoruz
from banka_sistemi import BankaMusterisi

# Sistemi test etmek için görsel sayfada bir müşteri oluşturuyoruz
musteri = BankaMusterisi("Can", "Öztürk", 45000, "1234")

# Butonlara tıklandığında çalışacak görsel fonksiyonlar
def baskan_giris_kontrol():
    pin = pin_giris.get()
    durum, mesaj = musteri.giris_yap(pin)
    
    if durum == "BAŞARILI":
        messagebox.showinfo("Banka Onayı", mesaj)
        # Giriş başarılıysa para yatırma alanını görünür yap
        islem_cercevesi.pack(pady=20)
        guncelle_bakiye_yazisi()
    elif durum == "HATA":
        messagebox.showwarning("Hatalı PIN", mesaj)
    else:
        messagebox.showerror("Güvenlik Engeli", mesaj)

def baskan_para_yatir():
    try:
        miktar = float(miktar_giris.get())
        sonuc_mesaji = musteri.para_yatir(miktar)
        messagebox.showinfo("İşlem Başarılı", sonuc_mesaji)
        guncelle_bakiye_yazisi()
        miktar_giris.delete(0, tk.END) # Kutuyu temizle
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def guncelle_bakiye_yazisi():
    bakiye_yazisi.config(text=f"Mevcut Bakiyeniz: {musteri.bakiye} TL")


# ---- TKINTER GÖRSEL TASARIM ALANI ----
pencere = tk.Tk()
pencere.title("Bankify Core - Güvenli ATM Sürümü")
pencere.geometry("450x400")
pencere.configure(bg="#1e1e2e") # Koyu şık bir arka plan rengi

# Başlık Yazısı
baslik = tk.Label(pencere, text="BANKIFY GÖRSEL ATM", font=("Arial", 16, "bold"), fg="#cdd6f4", bg="#1e1e2e")
baslik.pack(pady=15)

# GİRİŞ ALANI (PIN)
giris_cercevesi = tk.Frame(pencere, bg="#1e1e2e")
giris_cercevesi.pack(pady=10)

pin_etiket = tk.Label(giris_cercevesi, text="PIN Kodunuzu Girin:", font=("Arial", 11), fg="#cdd6f4", bg="#1e1e2e")
pin_etiket.grid(row=0, column=0, padx=5)

pin_giris = tk.Entry(giris_cercevesi, show="*", font=("Arial", 11), width=10, justify="center")
pin_giris.grid(row=0, column=1, padx=5)

giris_buton = tk.Button(giris_cercevesi, text="Giriş Yap", command=baskan_giris_kontrol, bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold"))
giris_buton.grid(row=0, column=2, padx=5)


# İŞLEM ALANI (Giriş yapana kadar gizli kalır)
islem_cercevesi = tk.Frame(pencere, bg="#313244", bd=2, relief="groove", padx=15, pady=15)

bakiye_yazisi = tk.Label(islem_cercevesi, text="Mevcut Bakiyeniz: 0 TL", font=("Arial", 12, "bold"), fg="#f5e0dc", bg="#313244")
bakiye_yazisi.pack(pady=5)

yatirma_etiket = tk.Label(islem_cercevesi, text="Yatırılacak Nakit Miktarı:", font=("Arial", 10), fg="#cdd6f4", bg="#313244")
yatirma_etiket.pack(pady=5)

miktar_giris = tk.Entry(islem_cercevesi, font=("Arial", 11), justify="center")
miktar_giris.pack(pady=5)

yatir_buton = tk.Button(islem_cercevesi, text="Nakit Yatır", command=baskan_para_yatir, bg="#89b4fa", fg="#11111b", font=("Arial", 10, "bold"))
yatir_buton.pack(pady=5)


# Programı pencereli modda çalıştırır
pencere.mainloop()
