import tkinter as tk
from tkinter import messagebox

hasap = 0

def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "sohbet" and password == "12345678":
        messagebox.showinfo("Başarılı Giriş", "Hoş geldiniz!")
        show_menu()
    else:
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya şifre yanlış!")

def show_menu():
    login_frame.pack_forget()
    menu_frame.pack()

def deposit():
    global hasap
    try:
        muktar = int(amount_entry.get())
        hasap += muktar
        messagebox.showinfo("Başarılı", f"Yeni Bakiyeniz: {hasap} TMT")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir miktar giriniz!")

def withdraw():
    global hasap
    try:
        muktar = int(amount_entry.get())
        if muktar > hasap:
            messagebox.showerror("Yetersiz Bakiye", f"Bakiyeniz: {hasap} TMT")
        else:
            hasap -= muktar
            messagebox.showinfo("Başarılı", f"Yeni Bakiyeniz: {hasap} TMT")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir miktar giriniz!")

def check_balance():
    messagebox.showinfo("Bakiyeniz", f"Güncel Bakiye: {hasap} TMT")

def transfer():
    global hasap
    try:
        kisi = recipient_entry.get()
        muktar = int(amount_entry.get())
        if muktar > hasap:
            messagebox.showerror("Yetersiz Bakiye", "Yeterli bakiye yok!")
        else:
            hasap -= muktar
            messagebox.showinfo("Başarılı", f"{kisi} kişisine {muktar} TMT transfer edildi!")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir miktar giriniz!")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Banka Sistemi")

login_frame = tk.Frame(root)
login_frame.pack()

tk.Label(login_frame, text="Kullanıcı Adı:").grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Şifre:").grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Giriş Yap", command=login).grid(row=2, columnspan=2)

menu_frame = tk.Frame(root)

tk.Label(menu_frame, text="İşlem Miktarı:").grid(row=0, column=0)
amount_entry = tk.Entry(menu_frame)
amount_entry.grid(row=0, column=1)

tk.Label(menu_frame, text="Kime (Transfer için):").grid(row=1, column=0)
recipient_entry = tk.Entry(menu_frame)
recipient_entry.grid(row=1, column=1)

tk.Button(menu_frame, text="Nakit Yatır", command=deposit).grid(row=2, column=0)
tk.Button(menu_frame, text="Nakit Çek", command=withdraw).grid(row=2, column=1)
tk.Button(menu_frame, text="Bakiye Kontrol", command=check_balance).grid(row=3, column=0)
tk.Button(menu_frame, text="Transfer", command=transfer).grid(row=3, column=1)
tk.Button(menu_frame, text="Çıkış", command=exit_app).grid(row=4, columnspan=2)

root.mainloop()