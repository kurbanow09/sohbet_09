import tkinter as tk
from tkinter import messagebox

soraglar = [
    ("Türkmenistanyň paýtagty nire?", ["Mary", "Daşoguz", "Aşgabat", "Türkmenbaşy"], "Aşgabat"),
    ("Dünýäniň iň beýik dagy haýsy?", ["Alp dagy", "Himalay", "Everest", "And"], "Everest"),
    ("Türkmenistanyň iň uly köli?", ["Hazar deňzi", "Karakum kanaly", "Sarygamyş köli", "Altyn köl"], "Hazar deňzi"),
    ("Gün ulgamynyň iň uly planetasy?", ["Wenera", "Ýupiter", "Mars", "Saturn"], "Ýupiter"),
    ("Taryhda ilkinji adam haçan Aýa gitdi?", ["1960", "1965", "1969", "1975"], "1969"),
    ("Elektrigi kim açdy?", ["Nikola Tesla", "Albert Eýnşteýn", "Benjamin Franklin", "Isaak Nyuton"], "Benjamin Franklin"),
    ("Türkmenistanyň baýdagyndaky ýyldyzlar näme aňladýar?", ["Milli bitewilik", "Şäherler", "Din", "Garaşsyzlyk"], "Şäherler"),
    ("Dünýäniň iň uzyn derýasy?", ["Amazon", "Nil", "Missisipi", "Yangze"], "Nil"),
    ("Kompýuteriň esasy gurluşy näme?", ["Monitor", "Klawiatura", "Protsessor", "Maus"], "Protsessor"),
    ("Ilkinji ýazygy kim döretdi?", ["Hytaýlylar", "Müsürliler", "Sumerler", "Grekler"], "Sumerler"),
]

bal = 0
dogry_jogap_sany = 0
sorag_indeksi = 0

def sorag_gorkez():
    global sorag_indeksi
    sorag, jogaplar, _ = soraglar[sorag_indeksi]
    sorag_label.config(text=f"Sorag {sorag_indeksi + 1}: {sorag}")
    for i in range(4):
        jogap_button[i].config(text=jogaplar[i])


def jogap_barlamak(indeks):
    global bal, dogry_jogap_sany, sorag_indeksi

    _, jogaplar, dogry_jogap = soraglar[sorag_indeksi]
    ulanyjy_jogaby = jogaplar[indeks]

    if ulanyjy_jogaby == dogry_jogap:
        messagebox.showinfo("Dogry Jogap!", "Dogry jogap! Bal gazandyň.")
        bal += 10
        dogry_jogap_sany += 1
    else:
        messagebox.showerror("Ýalňyş Jogap!", f"Ýalňyş jogap! Dogry jogap: {dogry_jogap}")
        bal -= 5

    sorag_indeksi += 1
    if sorag_indeksi < len(soraglar):
        sorag_gorkez()
    else:
        oýun_tamamlandy()

def oýun_tamamlandy():
    global bal, dogry_jogap_sany
    messagebox.showinfo(
        "Oýun Tamamlandy",
        f"Oýun tamamlandy! 🎉\nJemi bal: {bal}\nDogry jogaplaryň sany: {dogry_jogap_sany}",
    )
    root.destroy()

def oyuna_gir():
    giris.destroy()  
    oyun_basla()

def oyundan_cyk():
    giris.destroy()

def oyun_basla():
    global root, sorag_label, jogap_button

    root = tk.Tk()
    root.title("Milyoner Oýny")
    root.geometry("500x400")
    root.config(bg="#2e3f4f")  

    sorag_label = tk.Label(
        root, text="", font=("Helvetica", 14), wraplength=400, justify="center", bg="#2e3f4f", fg="white"
    )
    sorag_label.pack(pady=20)

    jogap_button = []
    for i in range(4):
        btn = tk.Button(
            root,
            text="",
            font=("Helvetica", 12),
            width=30,
            bg="#3498db",
            fg="white",
            command=lambda i=i: jogap_barlamak(i),
        )
        btn.pack(pady=5)
        jogap_button.append(btn)

    sorag_gorkez()
    root.mainloop()

giris = tk.Tk()
giris.title("Milyoner Oýny")
giris.geometry("400x300")
giris.config(bg="#34495e") 

title_label = tk.Label(
    giris,
    text="Milyoner Oýny",
    font=("Helvetica", 18, "bold"),
    bg="#34495e",
    fg="white",
)
title_label.pack(pady=50)

oyuna_gir_button = tk.Button(
    giris,
    text="Oýuna gir",
    font=("Helvetica", 14),
    bg="#3498db",
    fg="white",
    width=20,
    command=oyuna_gir,
)
oyuna_gir_button.pack(pady=10)

oyundan_cyk_button = tk.Button(
    giris,
    text="Oýundan çyk",
    font=("Helvetica", 14),
    bg="#e74c3c",
    fg="white",
    width=20,
    command=oyundan_cyk,
)
oyundan_cyk_button.pack(pady=10)

giris.mainloop()