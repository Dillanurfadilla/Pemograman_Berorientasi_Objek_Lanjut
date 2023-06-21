import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("650x650")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Kode_Anggota:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='nama:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='jK:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='prodi:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Alamat:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_anggota = Entry(mainFrame) 
        self.txtKode_anggota.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_anggota.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtnama = Entry(mainFrame) 
        self.txtnama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtjk = Entry(mainFrame) 
        self.txtjk.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtprodi = Entry(mainFrame) 
        self.txtprodi.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_anggota','kode_anggota','nama','jk','prodi','Alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_anggota', text='IDANGGOTA')
        self.tree.column('id_anggota', width="40")
        self.tree.heading('kode_anggota', text='KODE_ANGGOTA')
        self.tree.column('kode_anggota', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="100")
        self.tree.heading('jk', text='jK')
        self.tree.column('jk', width="30")
        self.tree.heading('prodi', text='prodi')
        self.tree.column('prodi', width="80")
        self.tree.heading('Alamat', text='Alamat')
        self.tree.column('Alamat', width="150")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,"")
        self.txtnama.delete(0,END)
        self.txtnama.insert(END,"")
        self.txtjk.delete(0,END)
        self.txtjk.insert(END,"")
        self.txtprodi.delete(0,END)
        self.txtprodi.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_anggota"],d["kode_anggota"],d["nama"],d["jk"],d["prodi"],d["Alamat"]))
    def onCari(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Anggota()
        a = obj.get_by_kode_anggota(kode_anggota)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Anggota()
        res = obj.get_by_kode_anggota(kode_anggota)
        self.txtKode_anggota.delete(0,END)
        self.txtKode_anggota.insert(END,obj.kode_anggota)
        self.txtnama.delete(0,END)
        self.txtnama.insert(END,obj.nama)
        self.txtjk.delete(0,END)
        self.txtjk.insert(END,obj.jk)
        self.txtprodi.delete(0,END)
        self.txtprodi.insert(END,obj.prodi)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.Alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_anggota = self.txtKode_anggota.get()
        Nama = self.txtnama.get()
        jk = self.txtjk.get()
        prodi = self.txtprodi.get()
        Alamat = self.txtAlamat.get()
        # create new Object
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        obj.nama = Nama
        obj.jk = jk
        obj.prodi = prodi
        obj.Alamat = Alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_anggota(kode_anggota)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_anggota = self.txtKode_anggota.get()
        obj = Anggota()
        obj.kode_anggota = kode_anggota
        if(self.ditemukan==True):
            res = obj.delete_by_kode_anggota(kode_anggota)
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
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()