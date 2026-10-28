import tkinter as tk
from tkinter import messagebox
from banka_sistemi import BankaMusterisi

gonderen_can = BankaMusterisi("Can", "Öztürk", 45000, "1234")
alici_merve = BankaMusterisi("Merve", "Yılmaz", 35000, "9999")

def baskan_giris_kontrol():
    pin = pin_giris.get()
    durum, mesaj = gonderen_can.giris_yap(pin)
    if durum == "BAŞARILI":
        messagebox.showinfo("Banka Onayı", mesaj)
        giris_ekrani_cercevesi.pack_forget()
        ana_menu_cercevesi.pack(pady=10, padx=10, fill="both", expand=True)
        guncelle_ekran_yazilari()
    elif durum == "HATA":
        messagebox.showwarning("Hatalı PIN", mesaj)
        pin_giris.delete(0, tk.END)
    else:
        messagebox.showerror("Güvenlik Engeli", mesaj)
        pin_giris.delete(0, tk.END)

def baskan_para_yatir():
    try:
        miktar = float(yatirma_giris.get())
        sonuc = gonderen_can.para_yatir(miktar)
        messagebox.showinfo("İşlem Başarılı", sonuc)
        guncelle_ekran_yazilari()
        yatirma_giris.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_kredi_basvurusu():
    try:
        miktar = float(kredi_giris.get())
        onayland_mi = gonderen_can.kredi_basvurusu_yap(miktar)
        if onayland_mi:
            messagebox.showinfo("Kredi Onayı", f"Tebrikler! {miktar} TL krediniz onaylandı ve hesabınıza aktarıldı.")
        else:
            messagebox.showwarning("Kredi Reddedildi", "Risk politikalarımız gereği kredi talebiniz reddedilmiştir.\n(Kredi skorunuzu yükseltmek için para yatırmayı deneyin).")
        guncelle_ekran_yazilari()
        kredi_giris.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_havale_yap():
    try:
        miktar = float(havale_giris.get())
        onayland_mi = gonderen_can.para_gonder(alici_merve, miktar)
        if onayland_mi:
            messagebox.showinfo("Transfer Başarılı", f"{alici_merve.isim} adlı kullanıcıya {miktar} TL başarıyla gönderildi.")
        else:
            messagebox.showwarning("Transfer Başarısız", "Bakiyeniz bu transfer için yetersizdir!")
        guncelle_ekran_yazilari()
        havale_giris.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def guncelle_ekran_yazilari():
    bakiye_yazisi.config(text=f"Mevcut Bakiyeniz: {gonderen_can.bakiye} TL")
    bilgi_paneli.config(text=f"Müşteri: {gonderen_can.isim} {gonderen_can.soyisim} | Kredi Skoru: {gonderen_can.kredi_skoru}")
    alici_bilgi.config(text=f"Kayıtlı Alıcı: {alici_merve.isim} {alici_merve.soyisim} ({alici_merve.hesap_no})")

# ---- TKINTER TASARIM ----
pencere = tk.Tk()
pencere.title("Bankify Core - Gelişmiş Görsel Bankacılık")
pencere.geometry("650x500")
pencere.configure(bg="#1e1e2e")

baslik = tk.Label(pencere, text="BANKIFY GÖRSEL ATM SİSTEMİ", font=("Arial", 18, "bold"), fg="#cdd6f4", bg="#1e1e2e")
baslik.pack(pady=10)

giris_ekrani_cercevesi = tk.Frame(pencere, bg="#313244", bd=2, relief="groove", padx=20, pady=20)
giris_ekrani_cercevesi.pack(pady=60)

tk.Label(giris_ekrani_cercevesi, text="Güvenli Kimlik Doğrulama", font=("Arial", 12, "bold"), fg="#a6e3a1", bg="#313244").pack(pady=10)
tk.Label(giris_ekrani_cercevesi, text="PIN Kodunuzu Girin (1234):", fg="#cdd6f4", bg="#313244").pack(pady=5)
pin_giris = tk.Entry(giris_ekrani_cercevesi, show="*", font=("Arial", 14), width=10, justify="center")
pin_giris.pack(pady=5)
tk.Button(giris_ekrani_cercevesi, text="Sisteme Giriş Yap", command=baskan_giris_kontrol, bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold"), padx=10, pady=5).pack(pady=15)

ana_menu_cercevesi = tk.Frame(pencere, bg="#1e1e2e")
bilgi_paneli = tk.Label(ana_menu_cercevesi, text="", font=("Arial", 10, "italic"), fg="#bac2de", bg="#1e1e2e")
bilgi_paneli.pack(pady=2)
bakiye_yazisi = tk.Label(ana_menu_cercevesi, text="", font=("Arial", 16, "bold"), fg="#f5e0dc", bg="#1e1e2e")
bakiye_yazisi.pack(pady=10)

paneller_arasi_bag = tk.Frame(ana_menu_cercevesi, bg="#1e1e2e")
paneller_arasi_bag.pack(pady=10, fill="both", expand=True)

sol_panel = tk.LabelFrame(paneller_arasi_bag, text=" Hesap ve Kredi İşlemleri ", font=("Arial", 11, "bold"), fg="#f9e2af", bg="#313244", padx=15, pady=15, bd=2)
sol_panel.pack(side="left", padx=15, fill="both", expand=True)

tk.Label(sol_panel, text="Nakit Yatırma Miktarı:", fg="#cdd6f4", bg="#313244").pack(pady=2)
yatirma_giris = tk.Entry(sol_panel, font=("Arial", 11), justify="center", width=15)
yatirma_giris.pack(pady=5)
tk.Button(sol_panel, text="Para Yatır", command=baskan_para_yatir, bg="#89b4fa", fg="#11111b", font=("Arial", 9, "bold")).pack(pady=5)

tk.Label(sol_panel, text="Talep Edilen Kredi:", fg="#cdd6f4", bg="#313244").pack(pady=10)
kredi_giris = tk.Entry(sol_panel, font=("Arial", 11), justify="center", width=15)
kredi_giris.pack(pady=5)
tk.Button(sol_panel, text="Kredi Başvurusu Yap", command=baskan_kredi_basvurusu, bg="#fab387", fg="#11111b", font=("Arial", 9, "bold")).pack(pady=5)

sag_panel = tk.LabelFrame(paneller_arasi_bag, text=" Havale / EFT Sistemi ", font=("Arial", 11, "bold"), fg="#a6e3a1", bg="#313244", padx=15, pady=15, bd=2)
sag_panel.pack(side="right", padx=15, fill="both", expand=True)

alici_bilgi = tk.Label(sag_panel, text="", font=("Arial", 9, "italic"), fg="#a6e3a1", bg="#313244")
alici_bilgi.pack(pady=5)
tk.Label(sag_panel, text="Gönderilecek Tutar (TL):", fg="#cdd6f4", bg="#313244").pack(pady=15)
havale_giris = tk.Entry(sag_panel, font=("Arial", 11), justify="center", width=15)
havale_giris.pack(pady=5)
tk.Button(sag_panel, text="Havale Gönder", command=baskan_havale_yap, bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold")).pack(pady=15)

pencere.mainloop()
