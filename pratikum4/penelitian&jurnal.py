print("\nNama: Dilla Nurfadilla")
print("\nNim: 210511086")
print("\nKelas: R2\n\n")

class Jurnal:
    def __init__(self,title,date):
        self.title = title
        self.date = date

class peneliti:
    def __init__(self,nama,jurnal):
        self.nama = nama
        self.jurnal = jurnal

    def daftar_jurnal(self):
        print(f'\nPeneliti\t:  {self.nama}\n')
        for jurnal in self.jurnal:
            print(f'Judul\t\t: ',jurnal.title)
            print(f'Published\t:  {jurnal.date}')
           
jurnal1 = Jurnal('Penerapan Data Mining Untuk Prediksi Pemasaran Produk Layanan Bank', 2019)
jurnal2 = Jurnal('Aplikasi Sistem Informasi Data Statistik Berbasis Web Di Badan Pusat Statistik Kabupaten Cirebon', 2018)
peneliti1 = peneliti('AS Dian Novianti', [jurnal1, jurnal2])
peneliti1.daftar_jurnal()
 