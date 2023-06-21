import tkinter as tk
from tkinter import Menu
from tkinter import *
from FrmBuku import *
from FrmAnggota import *
from FrmPeminjaman import *

# root window
root = tk.Tk()
root.title('perpus')
root.geometry("900x600")

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
# file_menu = Menu(menubar)
buku_menu = Menu(menubar)
peminjaman_menu = Menu(menubar)
anggota_menu = Menu(menubar)

# add a menu item to the menu
# file_menu.add_command(
#     label='File Open', command=root.destroy
# )

# file_menu.add_command(
#     label='Exit', command=root.destroy
# )

#menu anggota
anggota_menu.add_command(
    label='Anggota', command= lambda: new_window("data  anggota", FrmAnggota)
)


#menu buku
buku_menu.add_command(
    label='Buku', command= lambda: new_window("Daftar Buku", FrmBuku)
)

#menu anggota 
peminjaman_menu.add_command(
    label='Data peminjaman', command= lambda: new_window("Daftar Peminjaman", FrmPeminjaman)
)

# w = Label(root, fg = "white", compound =CENTER, image=gambar).pack(side="top")




def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)


# add the File menu to the menubar
# menubar.add_cascade(
#     label="File", menu=file_menu
# )

menubar.add_cascade(
    label="Pengguna", menu=anggota_menu
)
menubar.add_cascade(
    label="Buku", menu=buku_menu
)
menubar.add_cascade(
    label="Data Peminjaman", menu=peminjaman_menu
)

 
root.mainloop()