import tkinter as tk
from tkinter import scrolledtext
import config

def arayuz_insat_et(pencere):
    pencere.title(config.PENCERE_BASLIK)
    pencere.geometry(config.PENCERE_BOYUTU)
    pencere.configure(bg=config.RENK_ARKA_PLAN)

    # Üst Sabit Başlık
    baslik = tk.Label(pencere, text="BANKIFY ULTIMATE PREMIUM ATM", font=("Arial", 18, "bold"), fg=config.RENK_YAZI, bg=config.RENK_ARKA_PLAN)
    baslik.pack(pady=10)

    # 1. BÖLÜM: GİRİŞ EKRANI
    giris_cercevesi = tk.Frame(pencere, bg=config.RENK_KUTU_BG, bd=2, relief="groove", padx=20, pady=20)
    giris_cercevesi.pack(pady=150)
    
    tk.Label(giris_ekrani_cercevesi := giris_cercevesi, text="Güvenli Kimlik Doğrulama", font=("Arial", 12, "bold"), fg=config.RENK_YEŞİL, bg=config.RENK_KUTU_BG).pack(pady=10)
    tk.Label(giris_ekrani_cercevesi, text="PIN Kodunuzu Girin (1234):", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack(pady=5)
    pin_giris = tk.Entry(giris_ekrani_cercevesi, show="*", font=("Arial", 14), width=10, justify="center")
    pin_giris.pack(pady=5)
    giris_buton = tk.Button(giris_ekrani_cercevesi, text="Sisteme Giriş Yap", bg=config.RENK_YEŞİL, fg="#11111b", font=("Arial", 10, "bold"), padx=10, pady=5)
    giris_buton.pack(pady=15)

    # 2. BÖLÜM: ANA MENÜ ÇERÇEVESİ (Başlangıçta gizli)
    ana_menu_cercevesi = tk.Frame(pencere, bg=config.RENK_ARKA_PLAN)
    bilgi_paneli = tk.Label(ana_menu_cercevesi, text="", font=("Arial", 10, "italic"), fg="#bac2de", bg=config.RENK_ARKA_PLAN)
    bilgi_paneli.pack(pady=2)
    bakiye_yazisi = tk.Label(ana_menu_cercevesi, text="", font=("Arial", 16, "bold"), fg="#f5e0dc", bg=config.RENK_ARKA_PLAN)
    bakiye_yazisi.pack(pady=5)

    izgara_cerceve = tk.Frame(ana_menu_cercevesi, bg=config.RENK_ARKA_PLAN)
    izgara_cerceve.pack(pady=5, fill="both", expand=True)

    # Panel 1: Hesap ve Kredi
    panel1 = tk.LabelFrame(izgara_cerceve, text=" Hesap ve Kredi ", font=("Arial", 10, "bold"), fg=config.RENK_TURUNCU, bg=config.RENK_KUTU_BG, padx=10, pady=5)
    panel1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    tk.Label(panel1, text="Nakit Yatırma:", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack()
    yatirma_giris = tk.Entry(panel1, font=("Arial", 10), justify="center", width=12)
    yatirma_giris.pack(pady=2)
    yatir_buton = tk.Button(panel1, text="Para Yatır", bg=config.RENK_MAVİ, fg="#11111b", font=("Arial", 8, "bold"))
    yatir_buton.pack(pady=2)
    tk.Label(panel1, text="Kredi Talebi:", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack(pady=2)
    kredi_giris = tk.Entry(panel1, font=("Arial", 10), justify="center", width=12)
    kredi_giris.pack(pady=2)
    kredi_buton = tk.Button(panel1, text="Kredi İste", bg=config.RENK_TURUNCU, fg="#11111b", font=("Arial", 8, "bold"))
    kredi_buton.pack(pady=2)

    # Panel 2: Kredi Kartı İşlemleri
    panel2 = tk.LabelFrame(izgara_cerceve, text=" Kredi Kartı Dünyası ", font=("Arial", 10, "bold"), fg=config.RENK_PEMBE, bg=config.RENK_KUTU_BG, padx=10, pady=5)
    panel2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    kart_bilgi_etiket = tk.Label(panel2, text="", font=("Arial", 9), fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG)
    kart_bilgi_etiket.pack()
    tk.Label(panel2, text="Kartla Harcama Yap:", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack(pady=2)
    kart_harca_giris = tk.Entry(panel2, font=("Arial", 10), justify="center", width=12)
    kart_harca_giris.pack(pady=2)
    kart_harca_buton = tk.Button(panel2, text="Harcama Yap", bg=config.RENK_PEMBE, fg="#11111b", font=("Arial", 8, "bold"))
    kart_harca_buton.pack(pady=2)
    tk.Label(panel2, text="Kart Borcu Öde:", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack(pady=2)
    kart_ode_giris = tk.Entry(panel2, font=("Arial", 10), justify="center", width=12)
    kart_ode_giris.pack(pady=2)
    kart_ode_buton = tk.Button(panel2, text="Borç Öde", bg=config.RENK_YEŞİL, fg="#11111b", font=("Arial", 8, "bold"))
    kart_ode_buton.pack(pady=2)

    # Panel 3: Havale Sistemi
    panel3 = tk.LabelFrame(izgara_cerceve, text=" Havale / EFT ", font=("Arial", 10, "bold"), fg=config.RENK_YEŞİL, bg=config.RENK_KUTU_BG, padx=10, pady=5)
    panel3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    alici_bilgi = tk.Label(panel3, text="", font=("Arial", 9, "italic"), fg=config.RENK_YEŞİL, bg=config.RENK_KUTU_BG)
    alici_bilgi.pack()
    tk.Label(panel3, text="Gönderilecek Tutar:", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack(pady=5)
    havale_giris = tk.Entry(panel3, font=("Arial", 10), justify="center", width=12)
    havale_giris.pack(pady=2)
    havale_buton = tk.Button(panel3, text="Havale Gönder", bg=config.RENK_YEŞİL, fg="#11111b", font=("Arial", 8, "bold"))
    havale_buton.pack(pady=5)

    # Panel 4: Canlı Döviz Çevirici
    panel4 = tk.LabelFrame(izgara_cerceve, text=" ATM Döviz Masası ", font=("Arial", 10, "bold"), fg=config.RENK_MAVİ, bg=config.RENK_KUTU_BG, padx=10, pady=5)
    panel4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    tk.Label(panel4, text=f"Anlık Kurlar:\nDolar: {config.DOLAR_KURU} TL | Euro: {config.EURO_KURU} TL", font=("Arial", 9, "bold"), fg="#94e2d5", bg=config.RENK_KUTU_BG).pack()
    tk.Label(panel4, text="Çevrilecek TL Miktarı:", fg=config.RENK_YAZI, bg=config.RENK_KUTU_BG).pack(pady=2)
    doviz_giris = tk.Entry(panel4, font=("Arial", 10), justify="center", width=12)
    doviz_giris.pack(pady=2)
    doviz_buton = tk.Button(panel4, text="Dövize Çevir", bg=config.RENK_MAVİ, fg="#11111b", font=("Arial", 8, "bold"))
    doviz_buton.pack(pady=2)
    doviz_sonuc_etiket = tk.Label(panel4, text="", font=("Arial", 9, "bold"), fg=config.RENK_TURUNCU, bg=config.RENK_KUTU_BG)
    doviz_sonuc_etiket.pack(pady=2)

    izgara_cerceve.grid_columnconfigure(0, weight=1)
    izgara_cerceve.grid_columnconfigure(1, weight=1)

    # Panel 5: Dekont Bölümü
    log_cerceve = tk.LabelFrame(ana_menu_cercevesi, text=" Dijital Hesap Hareketleri (Dekont Ekranı) ", font=("Arial", 10, "bold"), fg="#bac2de", bg=config.RENK_DEKONT_BG, padx=10, pady=5)
    log_cerceve.pack(pady=10, fill="both", expand=True)
    log_ekrani = scrolledtext.ScrolledText(log_cerceve, width=80, height=8, font=("Courier", 9), bg=config.RENK_ARKA_PLAN, fg=config.RENK_YEŞİL, state=tk.DISABLED)
    log_ekrani.pack(fill="both", expand=True)

    # Tüm kutu ve elemanları ana sayfaya bir liste (Sözlük) halinde gönderiyoruz
    return {
        "giris_pnl": giris_cercevesi, "ana_pnl": ana_menu_cercevesi,
        "pin": pin_giris, "btn_giris": giris_buton,
        "bilgi": bilgi_paneli, "bakiye": bakiye_yazisi,
        "yatirma": yatirma_giris, "btn_yatir": yatir_buton,
        "kredi": kredi_giris, "btn_kredi": kredi_buton,
        "kart_bilgi": kart_bilgi_etiket, "kart_harca": kart_harca_giris, "btn_harca": kart_harca_buton,
        "kart_ode": kart_ode_giris, "btn_ode": kart_ode_buton,
        "alici": alici_bilgi, "havale": havale_giris, "btn_havale": havale_buton,
        "doviz": doviz_giris, "btn_doviz": doviz_buton, "doviz_snc": doviz_sonuc_etiket,
        "log": log_ekrani
    }
