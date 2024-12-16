import tkinter as tk
from tkinter import Button, Label, Entry
from tkinter.font import Font
from tkinter import messagebox

window = tk.Tk()
window.title("BIO DATA")
window.resizable(False, False)

bold_text= Font(family="Aerial", size=16, weight="bold", underline=1)

L1 = Label(window, text="Data Diri", font=bold_text)
L1.grid(row=0, column=0)

D1 = Label(window, text="Nama", font=("Aerial",12))
D1.grid(row=1, column=0)

D2 = Label(window, text="NIM", font=("Aerial",12))
D2.grid(row=2, column=0)

D3 = Label(window, text="Buku Favorit", font=("Aerial",12))
D3.grid(row=3, column=0)

D4 = Label(window, text="Motto", font=("Aerial",12))
D4.grid(row=4, column=0)

Masukkan = Entry(window, font=("Aerial",12))
Masukkan.grid(row=1, column= 1, padx=10, pady=10)

Masukkan = Entry(window, font=("Aerial",12))
Masukkan.grid(row=2, column= 1, padx=10, pady=10)

Masukkan = Entry(window, font=("Aerial",12))
Masukkan.grid(row=3, column= 1, padx=10, pady=10)

Masukkan = Entry(window, font=("Aerial",12))
Masukkan.grid(row=4, column= 1, padx=10, pady=10)

def hapus():
    window.destroy()

B = Button(window, text="Keluar", command=hapus, width=10 )
B.grid(row=5, column= 1, padx=10, pady=10)

def submit():
    messagebox.showinfo(text="data terkirim")

S = Button(window, text="Submit", command=submit, width=10)
S.grid(row=5, column= 1, padx=10, pady=10)

window.mainloop()

