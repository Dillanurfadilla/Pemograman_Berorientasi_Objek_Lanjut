class Mahasiswa:
    def __init__(self, nama, kelas, nim, prodi):
        self.nama = nama
        self.kelas = kelas
        self.nim = nim
        self.prodi = prodi

class Kelompok_KKN:
    def __init__(self, nomor_kelompok, Mahasiswa):
        self.nomor_keompok = nomor_kelompok
        self.Mahasiwa = Mahasiswa
    def pemilihan_kelompok(self):
        for Mahasiswa in self.Mahasiwa:
            print(Mahasiswa.nama, Mahasiswa.kelas, Mahasiswa.nim, Mahasiswa.prodi)

Mahasiswa1 = Mahasiswa("Ryunjin", 1, "200512085", "Ilmu_Komputer")
Mahasiswa2 = Mahasiswa("Hyunjun", 3, "200504032", "Teknik_informatika")

Kelompok_KKN = Kelompok_KKN("44", [Mahasiswa1, Mahasiswa2])
Kelompok_KKN.pemilihan_kelompok()