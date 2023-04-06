print("\nNama: Dilla Nurfadilla")
print("\nNim: 210511086")
print("\nKelas: R2\n\n")

class Penulis:
    def __init__(self,nama):
        self.nama = nama
        self.inventory = Inventory()
    
    def tampil(self):
        print(f'\nPenulis\t\t:  {self.nama}\n')

class Buku:
    def __init__(self,judul,publish,penerbit):
        self.judul = judul
        self.publish = publish
        self.penerbit = penerbit

    def get_judul(self):
        return self.judul

    def get_publish(self):
        return self.publish

    def get_penerbit(self):
        return self.penerbit

class Inventory:
    def __init__(self):
        self.books = []

    def add_buku(self,buku):
        self.books.append(buku)

    def daftar_buku(self):
        for buku in self.books:
            print(f'Judul\t\t: ',buku.judul)
            print(f'Terbit\t\t: ',buku.publish)
            print(f'Penerbit\t: ',buku.penerbit)

penulis1 = Penulis('jk_Rowling')
Harry_Potter = Buku('Harry_Potter and The Sorcerers Stone', 'Britania Raya, 1997', 'Britania Raya')
Harry_Potter = Buku('Harry Potter and the Chamber of Secrets', 'Britania Raya, 1998', 'Britania Raya')
Harry_Potter = Buku('Harry Potter and The Prisoner of Azkaban', 'Britania Raya, 19999', 'Britania Raya')
penulis1.inventory.add_buku(Harry_Potter)
penulis1.inventory.add_buku(Harry_Potter)
penulis1.inventory.add_buku(Harry_Potter)
penulis1.inventory.books
penulis1.tampil()
penulis1.inventory.daftar_buku()