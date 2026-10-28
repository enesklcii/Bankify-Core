import tkinter as tk
from tkinter import messagebox
from banka_beyni import BankaMusterisi
import arayuz_elemanlari
import config

# Müşteri Verilerini Tanımlıyoruz
gonderen_can = BankaMusterisi("Can", "Öztürk", 45000, "1234")
alici_merve = BankaMusterisi("Merve", "Yılmaz", 35000, "9999")

# Pencereyi Başlat
pencere = tk.Tk()

# Arayüz iskeletini inşa et ve elemanları sözlük olarak al
ui = arayuz_elemanlari.arayuz_insat_et(pencere)

# ---- MOTOR FONKSİYONLAR (İŞLEMLER) ----

def yenile_log_ekrani():
    try:
        with open("banka_loglari.txt", "r", encoding="utf-8") as dosya:
            loglar = dosya.readlines()
        ui["log"].config(state=tk.NORMAL)
        ui["log"].delete(1.0, tk.END)
        for log in reversed(loglar):
            ui["log"].insert(tk.END, log)
        ui["log"].config(state=tk.DISABLED)
    except FileNotFoundError:
        pass

def guncelle_ekran_yazilari():
    ui["bakiye"].config(text=f"Mevcut Hesap Bakiyeniz: {gonderen_can.bakiye} TL")
    ui["bilgi"].config(text=f"Müşteri: {gonderen_can.isim} {gonderen_can.soyisim} | Kredi Skoru: {gonderen_can.kredi_skoru}")
    ui["alici"].config(text=f"Kayıtlı Alıcı: {alici_merve.isim} {alici_merve.soyisim} ({alici_merve.hesap_no})")
    ui["kart_bilgi"].config(text=f"Kart Limiti: {gonderen_can.kart_limiti} TL | Güncel Borç: {gonderen_can.kart_borcu} TL\nKalan Limit: {gonderen_can.kart_limiti - gonderen_can.kart_borcu} TL")

def baskan_giris_kontrol():
    pin = ui["pin"].get()
    durum, mesaj = gonderen_can.giris_yap(pin)
    if durum == "BAŞARILI":
        messagebox.showinfo("Banka Onayı", mesaj)
        ui["giris_pnl"].pack_forget()
        ui["ana_pnl"].pack(pady=5, padx=10, fill="both", expand=True)
        guncelle_ekran_yazilari()
        yenile_log_ekrani()
    elif durum == "HATA":
        messagebox.showwarning("Hatalı PIN", mesaj)
        ui["pin"].delete(0, tk.END)
    else:
        messagebox.showerror("Güvenlik Engeli", mesaj)
        ui["pin"].delete(0, tk.END)

def baskan_para_yatir():
    try:
        miktar = float(ui["yatirma"].get())
        sonuc = gonderen_can.para_yatir(miktar)
        messagebox.showinfo("İşlem Başarılı", sonuc)
        guncelle_ekran_yazilari()
        yenile_log_ekrani()
        ui["yatirma"].delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_kredi_basvurusu():
    try:
        miktar = float(ui["kredi"].get())
        onaylandi_mi = gonderen_can.kredi_basvurusu_yap(miktar)
        if onaylandi_mi:
            messagebox.showinfo("Kredi Onayı", f"Tebrikler! {miktar} TL krediniz onaylandı.")
        else:
            messagebox.showwarning("Kredi Reddedildi", "Risk politikalarımız gereği kredi talebiniz reddedilmiştir.")
        guncelle_ekran_yazilari()
        yenile_log_ekrani()
        ui["kredi"].delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_havale_yap():
    try:
        miktar = float(ui["havale"].get())
        onaylandi_mi = gonderen_can.para_gonder(alici_merve, miktar)
        if onaylandi_mi:
            messagebox.showinfo("Transfer Başarılı", f"{alici_merve.isim} adlı kullanıcıya {miktar} TL gönderildi.")
        else:
            messagebox.showwarning("Transfer Başarısız", "Bakiyeniz yetersizdir!")
        guncelle_ekran_yazilari()
        yenile_log_ekrani()
        ui["havale"].delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_kart_harca():
    try:
        miktar = float(ui["kart_harca"].get())
        durum, mesaj = gonderen_can.kartla_harca(miktar)
        if durum == "BAŞARILI":
            messagebox.showinfo("Kart Onayı", mesaj)
        else:
            messagebox.showwarning("Kart Hatası", mesaj)
        guncelle_ekran_yazilari()
        yenile_log_ekrani()
        ui["kart_harca"].delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_kart_borc_ode():
    try:
        miktar = float(ui["kart_ode"].get())
        durum, mesaj = gonderen_can.kart_borcu_ode(miktar)
        if durum == "BAŞARILI":
            messagebox.showinfo("Ödeme Onayı", mesaj)
        else:
            messagebox.showwarning("Ödeme Hatası", mesaj)
        guncelle_ekran_yazilari()
        yenile_log_ekrani()
        ui["kart_ode"].delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def baskan_doviz_hesapla():
    try:
        tl_miktar = float(ui["doviz"].get())
        dolar_sonuc = tl_miktar / config.DOLAR_KURU
        euro_sonuc = tl_miktar / config.EURO_KURU
        ui["doviz_snc"].config(text=f"Dolar karşılığı: ${dolar_sonuc:.2f}\nEuro karşılığı: €{euro_sonuc:.2f}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir TL miktarı girin!")


# ---- BUTONLARIN COMMAND TETİKLEYİCİLERİNİ BAĞLIYORUZ ----
ui["btn_giris"].config(command=baskan_giris_kontrol)
ui["btn_yatir"].config(command=baskan_para_yatir)
ui["btn_kredi"].config(command=baskan_kredi_basvurusu)
ui["btn_harca"].config(command=baskan_kart_harca)
ui["btn_ode"].config(command=baskan_kart_borc_ode)
ui["btn_havale"].config(command=baskan_havale_yap)
ui["btn_doviz"].config(command=baskan_doviz_hesapla)

# Döngüyü Başlat
pencere.mainloop()
