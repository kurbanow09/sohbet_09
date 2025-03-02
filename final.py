import tkinter as tk
from tkinter import messagebox
import random
import time

soraglar = [
    ("Python'da bir sanawa nädip döretmeli?", ["list()", "{}", "[]", "()"], "[]"),
    ("Python'da bir funksiýa nädip tanatylýar?", ["def", "function", "func", "lambda"], "def"),
    ("Python'da öwrüm nädip başlamaly?", ["for", "foreach", "while", "loop"], "for"),
    ("Python'da bir üýtgeýji nädip tanatylýar?", ["var", "let", "const", "None"], "None"),
    ("Python'da bir sözlük nädip tanatylýar?", ["dict()", "map()", "{}", "[]"], "{}"),
    ("Python'da bir san nädip tanatylýar?", ["int()", "float()", "str()", "number()"], "int()"),
    ("Python'da bir string nädip bölinýär?", ["split()", "divide()", "cut()", "separate()"], "split()"),
    ("Python'da bir san nädip string edilýär?", ["str()", "int()", "float()", "toString()"], "str()"),
    ("Python'da bir string nädip san edilýär?", ["int()", "str()", "float()", "parseInt()"], "int()"),
    ("Python'da bir faýl nädip açylýar?", ["open()", "file()", "read()", "write()"], "open()"),
    ("Python'da bir faýl nädip ýazylar?", ["write()", "print()", "log()", "save()"], "write()"),
    ("Python'da bir faýl nädip ýapylýar?", ["close()", "end()", "stop()", "finish()"], "close()"),
    ("Python'da bir faýl nädip okalýar?", ["read()", "open()", "load()", "fetch()"], "read()"),
    ("Python'da bir sanawdan element nädip aýrylýar?", ["remove()", "delete()", "pop()", "discard()"], "remove()"),
    ("Python'da bir element sanawa nädip goşulýar?", ["add()", "append()", "insert()", "push()"], "append()"),
    ("Python'da logika operasiýalar nädip işleýär?", ["and, or, not", "&&, ||, !", "and, or, no", "&&, ||, not"], "and, or, not"),
    ("Python'da bir modul nädip import edilýär?", ["import", "include", "require", "fetch"], "import"),
    ("Python'da öwüt nädip ýazylýar?", ["#", "//", "/*", "<!--"], "#"),
    ("Python'da bir synp nädip tanatylýar?", ["class", "def", "function", "object"], "class"),
    ("Python'da bir synp nädip miras alýar?", ["inherit()", "extend()", "super()", "base()"], "inherit()"),
    ("Python'da bir funksiýa nädip çagyrlar?", ["call()", "invoke()", "execute()", "run()"], "call()"),
    ("Python'da setir nädip birikdirilýär?", ["+", "&", "concat", "join"], "+"),
    ("Python'da öwrüm nädip tamamlanýar?", ["break", "exit", "stop", "end"], "break"),
    ("Python'da bir hat nädip dolandyrylýar?", ["try, except", "catch, except", "try, catch", "except, catch"], "try, except"),
    ("Python'da bir modul nädip döredilýär?", ["create", "define", "module", "import"], "import"),
    ("Python'da bir san nädip goşulýar?", ["+", "-", "*", "/"], "+"),
    ("Python'da bir san nädip aýrylýar?", ["-", "+", "*", "/"], "-"),
    ("Python'da bir san nädip köpeldilýär?", ["*", "+", "-", "/"], "*"),
    ("Python'da bir san nädip bölünýär?", ["/", "*", "+", "-"], "/"),
    ("Python'da bir san nädip goşulýar?", ["sum()", "add()", "total()", "count()"], "sum()"),
    ("Python'da bir san nädip aýrylýar?", ["sub()", "subtract()", "minus()", "deduct()"], "subtract()"),
    ("Python'da bir san nädip köpeldilýär?", ["mul()", "multiply()", "times()", "product()"], "multiply()"),
    ("Python'da bir san nädip bölünýär?", ["div()", "divide()", "cut()", "split()"], "divide()"),
    ("Python'da bir sanaw nädip tersine öwrülýär?", ["reverse()", "invert()", "flip()", "turn()"], "reverse()"),
    ("Python'da sanawyň uzynlygyny nädip tapmaly?", ["len()", "length()", "size()", "count()"], "len()"),
    ("Python'da sanawda element barmy nädip barlamaly?", ["in", "exists", "contains", "has"], "in"),
    ("Python'da sanawyň iň uly elementini nädip tapmaly?", ["max()", "largest()", "biggest()", "top()"], "max()"),
    ("Python'da sanawyň iň kiçi elementini nädip tapmaly?", ["min()", "smallest()", "tiny()", "bottom()"], "min()"),
    ("Python'da sanawyň elementlerini nädip sanamaly?", ["count()", "enumerate()", "number()", "list()"], "count()"),
    ("Python'da sanawyň elementlerini nädip düzmeli?", ["sort()", "order()", "arrange()", "lineup()"], "sort()"),
    ("Python'da sanawyň elementlerini nädip goşmaly?", ["+", "add()", "append()", "concat()"], "append()"),
    ("Python'da sanawda element nädip üýtgetmeli?", ["set()", "change()", "modify()", "update()"], "set()"),
    ("Python'da sanawda element nädip aýyrmaly?", ["remove()", "delete()", "discard()", "erase()"], "remove()"),
    ("Python'da sanawyň elementlerini nädip arassalamaly?", ["clear()", "delete()", "empty()", "wipe()"], "clear()"),
    ("Python'da sanawyň elementlerini nädip göçürmeli?", ["copy()", "clone()", "duplicate()", "mirror()"], "copy()"),
    ("Python'da sanawyň elementlerini nädip birleşdirmeli?", ["extend()", "join()", "combine()", "merge()"], "extend()"),
    ("Python'da stringi nädip sanawa öwürmeli?", ["split()", "divide()", "separate()", "cut()"], "split()"),
    ("Python'da sanawy nädip stringe öwürmeli?", ["join()", "concat()", "combine()", "merge()"], "join()"),
    ("Python'da stringi nädip uly harp bilen ýazmaly?", ["upper()", "capitalize()", "big()", "uppercase()"], "upper()"),
    ("Python'da stringi nädip kiçi harp bilen ýazmaly?", ["lower()", "small()", "tiny()", "lowercase()"], "lower()"),
    ("Python'da stringi nädip baş harp bilen ýazmaly?", ["capitalize()", "title()", "headline()", "upper()"], "capitalize()"),
    ("Python'da stringi nädip boşluklardan arassalamaly?", ["strip()", "clean()", "trim()", "remove()"], "strip()"),
    ("Python'da stringi nädip bölekleýin almak?", ["slice()", "cut()", "split()", "divide()"], "slice()"),
    ("Python'da san nädip integere öwürmeli?", ["int()", "toInteger()", "convert()", "parseInt()"], "int()"),
    ("Python'da san nädip floaty öwürmeli?", ["float()", "toFloat()", "convert()", "parseFloat()"], "float()"),
]

bal = 0
dogry_jogap_sany = 0
sorag_indeksi = 0
kalan_sure = 180  
secili_soraglar = random.sample(soraglar, 25)

def sorag_gorkez():
    global sorag_indeksi, kalan_sure
    sorag, jogaplar, _ = secili_soraglar[sorag_indeksi]
    random.shuffle(jogaplar)  
    sorag_label.config(text=f"Sorag {sorag_indeksi + 1}: {sorag}")
    for i in range(4):
        jogap_button[i].config(text=jogaplar[i])
    kalan_sure = 180
    sure_guncelle()

def jogap_barlamak(indeks):
    global bal, dogry_jogap_sany, sorag_indeksi, kalan_sure

    _, jogaplar, dogry_jogap = secili_soraglar[sorag_indeksi]
    ulanyjy_jogaby = jogaplar[indeks]

    if ulanyjy_jogaby == dogry_jogap:
        messagebox.showinfo("Dogry Jogap!", "Dogry jogap! Bal gazandyň.")
        bal += 10
        dogry_jogap_sany += 1
    else:
        messagebox.showerror("Ýalňyş Jogap!", f"Ýalňyş jogap! Dogry jogap: {dogry_jogap}")
        bal -= 5

    sorag_indeksi += 1
    if sorag_indeksi < len(secili_soraglar):
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

def sure_guncelle():
    global kalan_sure, sorag_indeksi
    if kalan_sure > 0:
        kalan_sure -= 1
        sure_label.config(text=f"Galan minut: {kalan_sure} sekunt")
        root.after(1000, sure_guncelle)
    else:
        messagebox.showerror("Oyun gutardy mal!", "Gandon Oyun gutardy! Geçerli Name jogap bermedin huy.")
        sorag_indeksi += 1
        if sorag_indeksi < len(secili_soraglar):
            sorag_gorkez()
        else:
            oýun_tamamlandy()

def oyuna_gir():
    giris.destroy()  
    oyun_basla()

def oyundan_cyk():
    giris.destroy()

def oyun_basla():
    global root, sorag_label, jogap_button, sure_label

    root = tk.Tk()
    root.title("Python Öğrenme Oyunu")
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

    sure_label = tk.Label(
        root, text="", font=("Helvetica", 12), bg="#2e3f4f", fg="white"
    )
    sure_label.pack(pady=10)

    sorag_gorkez()
    root.mainloop()

giris = tk.Tk()
giris.title("Python😉")
giris.geometry("400x300")
giris.config(bg="#34495e") 

title_label = tk.Label(
    giris,
    text="Python😉",
    font=("Helvetica", 18, "bold"),
    bg="#34495e",
    fg="white",
)
title_label.pack(pady=50)

oyuna_gir_button = tk.Button(
    giris,
    text="Oyuna gir",
    font=("Helvetica", 14),
    bg="#3498db",
    fg="white",
    width=20,
    command=oyuna_gir,
)
oyuna_gir_button.pack(pady=10)

oyundan_cyk_button = tk.Button(
    giris,
    text="Oyundan çık",
    font=("Helvetica", 14),
    bg="#e74c3c",
    fg="white",
    width=20,
    command=oyundan_cyk,
)
oyundan_cyk_button.pack(pady=10)

giris.mainloop()