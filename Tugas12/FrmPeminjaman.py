import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("850x850")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NOMOR_BUKTI:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_ANGGOTA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_PINJAM:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_KEMBALI:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE_BUKU:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNomor_bukti = Entry(mainFrame) 
        self.txtNomor_bukti.grid(row=0, column=1, padx=5, pady=5)
        self.txtNomor_bukti.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txttanggal_pinjam= Entry(mainFrame) 
        self.txttanggal_pinjam.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txttanggal_kembali = Entry(mainFrame) 
        self.txttanggal_kembali.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtkode_buku = Entry(mainFrame) 
        self.txtkode_buku.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_pinjam','nomor_bukti','kode_anggota','tanggal_pinjam','tanggal_kembali', 'kode_buku')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pinjam', text='IDPINJAM')
        self.tree.column('id_pinjam', width="40")
        self.tree.heading('nomor_bukti', text='NOMOR_BUKTI')
        self.tree.column('nomor_bukti', width="100")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('tanggal_pinjam', text='TANGGAL_PINJAM')
        self.tree.column('tanggal_pinjam', width="120")
        self.tree.heading('tanggal_kembali', text='TANGGAL_KEMBALI')
        self.tree.column('tanggal_kembali', width="120")
        self.tree.heading('kode_buku', text='KODE_BUKU')
        self.tree.column('kode_buku', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNomor_bukti.delete(0,END)
        self.txtNomor_bukti.insert(END,"")
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txttanggal_pinjam.delete(0,END)
        self.txttanggal_pinjam.insert(END,"")
        self.txttanggal_kembali.delete(0,END)
        self.txttanggal_kembali.insert(END,"")
        self.txtkode_buku.delete(0,END)
        self.txtkode_buku.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)   

        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["kode_pinjam"],d["nomor_bukti"],d["kode_anggota"],d["tanggal_pinjam"],d["tanggal_kembali"],d["kode_buku"]))
    def onCari(self, event=None):
        nomor_bukti = self.txtNomor_bukti.get()
        obj = Peminjaman()
        a = obj.get_by_nomor_bukti(nomor_bukti)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nomor_bukti = self.txtNomor_bukti.get()
        obj = Peminjaman()
        res = obj.get_by_nomor_bukti(nomor_bukti)
        self.txtNomor_bukti.delete(0,END)
        self.txtNomor_bukti.insert(END,obj.nomor_bukti)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txttanggal_pinjam.delete(0,END)
        self.txttanggal_pinjam.insert(END,obj.tanggal_pinjam)
        self.txttanggal_kembali.delete(0,END)
        self.txttanggal_kembali.insert(END,obj.tanggal_kembali)
        self.txtkode_buku.delete(0,END)
        self.txtkode_buku.insert(END,obj.kode_buku)
        
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nomor_bukti = self.txtNomor_bukti.get()
        kode_anggota = self.txtKode_anggota.get()
        tanggal_pinjam = self.txttanggal_pinjam.get()
        tanggal_kembali = self.txttanggal_kembali.get()
        kode_buku = self.txtkode_buku.get()
        # create new Object
        obj = Peminjaman()
        obj.nomor_bukti = nomor_bukti
        obj.kode_anggota = kode_anggota
        obj.tanggal_pinjam = tanggal_pinjam
        obj.tanggal_kembali = tanggal_kembali
        obj.kode_buku = kode_buku
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nomor_bukti(nomor_bukti)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nomor_bukti = self.txtNomor_bukti.get()
        obj = Peminjaman()
        obj.nomor_bukti = nomor_bukti
        if(self.ditemukan==True):
            res = obj.delete_by_nomor_bukti(nomor_bukti)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()