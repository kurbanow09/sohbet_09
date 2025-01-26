import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("Paýhasly Sözler")
root.geometry("400x600")
root.configure(bg="black")

current_theme = {"bg": "black", "fg": "white", "btn_bg": "#007BFF", "btn_fg": "white"}

quotes = [
    "Durmuş bir aýnadyr; oňa nähili seretseň, saňa şeýleräk görkezer.",
    "Üstünlik sabyrlylygyň we zähmetsöýerligiň miwesidir.",
    "Ekin ekmeseň, hasyl almazsyň.",
    "Ýagşynyň kömegi, güneşiň ýagtysy ýaly.",
    "Bilik gazanan hiç haçan azaşmaz.",
    "Taryhyny bilýän millet güýçlidir.",
]

favorites = []

current_frame = None


def switch_frame(new_frame):
    global current_frame
    if current_frame is not None:
        current_frame.pack_forget()
    new_frame.pack(fill="both", expand=True)
    current_frame = new_frame


home_frame = tk.Frame(root, bg=current_theme["bg"])


def go_home():
    switch_frame(home_frame)


def update_theme():
    root.configure(bg=current_theme["bg"])
    for frame in [home_frame, list_frame, favorites_frame]:
        frame.configure(bg=current_theme["bg"])
    listbox.configure(bg=current_theme["bg"], fg=current_theme["fg"])
    fav_listbox.configure(bg=current_theme["bg"], fg=current_theme["fg"])


def show_message():
    messagebox.showinfo("Operator", "+993-63-69-68-68")


label = tk.Label(home_frame, text="Paýhasly Sözler", font=("Arial", 20), bg=current_theme["bg"], fg=current_theme["fg"])
label.pack(pady=20)
label.bind("<Button-1>", lambda e: show_message())

tk.Button(home_frame, text="Sözleriň Sanawy", command=lambda: switch_frame(list_frame), bg=current_theme["btn_bg"], fg=current_theme["btn_fg"], font=("Arial", 14)).pack(pady=10)
tk.Button(home_frame, text="Halaýanlary Gör", command=lambda: switch_frame(favorites_frame), bg=current_theme["btn_bg"], fg=current_theme["btn_fg"], font=("Arial", 14)).pack(pady=10)
tk.Button(home_frame, text="Temany Üýtget", command=lambda: open_theme_window(), bg=current_theme["btn_bg"], fg=current_theme["btn_fg"], font=("Arial", 14)).pack(pady=10)
tk.Button(home_frame, text="Çykmak", command=root.quit, bg="red", fg="white", font=("Arial", 14)).pack(pady=20)

list_frame = tk.Frame(root, bg=current_theme["bg"])


def update_list():
    listbox.delete(0, tk.END)
    for quote in quotes:
        listbox.insert(tk.END, quote)


listbox = tk.Listbox(list_frame, width=40, height=20, bg=current_theme["bg"], fg=current_theme["fg"], selectbackground="gray", font=("Arial", 12))
listbox.pack(pady=10)


def search_quote():
    search_term = simpledialog.askstring("Gözleg", "Gözlemek isleýän sözüňizi giriziň:", parent=root)
    if search_term:
        matching_quotes = [q for q in quotes if search_term.lower() in q.lower()]
        listbox.delete(0, tk.END)
        for quote in matching_quotes:
            listbox.insert(tk.END, quote)
        if not matching_quotes:
            messagebox.showinfo("Netije", "Gözlenen söz tapylmady!")
    else:
        update_list()


def add_new_quote():
    new_quote = simpledialog.askstring("Täze Söz", "Täze sözi giriziň:", parent=root)
    if new_quote:
        if new_quote not in quotes:
            quotes.append(new_quote)
            update_list()
            messagebox.showinfo("Üstünlik", "Täze söz sanawa goşuldy!")
        else:
            messagebox.showinfo("Duýduryş", "Bu söz eýýäm sanawda bar!")


def add_to_favorites():
    selected = listbox.curselection()
    if selected:
        quote = listbox.get(selected)
        if quote not in favorites:
            favorites.append(quote)
            update_favorites()
            messagebox.showinfo("Üstünlik", "Söz halaýanlara goşuldy!")
        else:
            messagebox.showinfo("Maglumat", "Bu söz eýýäm halaýanlaryň arasynda.")
    else:
        messagebox.showinfo("Duýduryş", "Halaýanlara goşmak üçin bir sözi saýlaň!")
def remove_quote():
    selected = listbox.curselection()
    if selected:
        quote = listbox.get(selected)
        quotes.remove(quote)
        update_list()
        messagebox.showinfo("Üstünlik", "Söz pozuldy!")
    else:
        messagebox.showinfo("Duýduryş", "Pozmak üçin bir sözi saýlaň!")


tk.Button(list_frame, text="Söz Pozmak", command=remove_quote, bg="red", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(list_frame, text="Halaýanlaryma Goş", command=add_to_favorites, bg=current_theme["btn_bg"], fg=current_theme["btn_fg"], font=("Arial", 12)).pack(pady=5)
tk.Button(list_frame, text="Täze Söz Goşmak", command=add_new_quote, bg="#007BFF", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(list_frame, text="Gözleg", command=search_quote, bg="green", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(list_frame, text="Baş Sahypa", command=go_home, bg=current_theme["btn_bg"], fg=current_theme["btn_fg"], font=("Arial", 12)).pack(pady=5)

favorites_frame = tk.Frame(root, bg=current_theme["bg"])


def update_favorites():
    fav_listbox.delete(0, tk.END)
    for favorite in favorites:
        fav_listbox.insert(tk.END, favorite)


fav_listbox = tk.Listbox(favorites_frame, width=40, height=20, bg=current_theme["bg"], fg=current_theme["fg"], selectbackground="gray", font=("Arial", 12))
fav_listbox.pack(pady=10)


def remove_from_favorites():
    selected = fav_listbox.curselection()
    if selected:
        quote = fav_listbox.get(selected)
        favorites.remove(quote)
        update_favorites()
        messagebox.showinfo("Üstünlik", "Söz halaýanlardan aýryldy!")
    else:
        messagebox.showinfo("Duýduryş", "Aýyrmak üçin bir sözi saýlaň!")


tk.Button(favorites_frame, text="Halaýanlardan Aýyr", command=remove_from_favorites, bg="red", fg="white", font=("Arial", 14)).pack(pady=10)
tk.Button(favorites_frame, text="Baş Sahypa", command=go_home, bg=current_theme["btn_bg"], fg=current_theme["btn_fg"], font=("Arial", 14)).pack(pady=10)


def open_theme_window():
    theme_window = tk.Toplevel(root)
    theme_window.title("Temany Üýtget")
    theme_window.geometry("300x200")
    theme_window.configure(bg=current_theme["bg"])

    def set_theme(bg, fg, btn_bg, btn_fg):
        current_theme.update({"bg": bg, "fg": fg, "btn_bg": btn_bg, "btn_fg": btn_fg})
        update_theme()
        theme_window.destroy()

    tk.Button(theme_window, text="Ak Tema", command=lambda: set_theme("white", "black", "#007BFF", "white"), font=("Arial", 14)).pack(pady=10)
    tk.Button(theme_window, text="Gara Tema", command=lambda: set_theme("black", "white", "#007BFF", "white"), font=("Arial", 14)).pack(pady=10)
    tk.Button(theme_window, text="Gyzyl Tema", command=lambda: set_theme("red", "white", "#007BFF", "white"), font=("Arial", 14)).pack(pady=10)
    tk.Button(theme_window, text="Gök Tema", command=lambda: set_theme("blue", "white", "#007BFF", "white"), font=("Arial", 14)).pack(pady=10)


switch_frame(home_frame)
update_list()
update_favorites()

root.mainloop()
