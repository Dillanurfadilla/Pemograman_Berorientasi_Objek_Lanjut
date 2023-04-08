class Penulis:
    def __init__(self, nama, buku):
        self.nama = nama
        self.buku = buku

class Buku:
    def __init__(self, nama, penulis):
        self.nama = nama
        self.penulis = penulis
    
    def daftar_buku(self):
        for Penulis in self.penulis:
            print(Penulis.nama, Penulis.buku)

Penulis1 = Penulis("Senja", "Edward")
Penulis2 = Penulis("Sunyi", "Laras")

Buku = Buku("Karya", [Penulis1, Penulis2])
Buku.daftar_buku()