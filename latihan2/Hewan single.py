class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def bergerak(self):
            print (self.nama, "bergerak")

class kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("Meow")

KucingA = kucing("Kitty", 2, "Persia")
KucingA.bergerak() # output : Kitty bergerak
KucingA.bersuara() # output : Meow!

