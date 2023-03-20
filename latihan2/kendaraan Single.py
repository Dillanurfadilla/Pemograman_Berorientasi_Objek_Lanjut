class kendaraan:
    def __init__(self, jenis, merek, warna):
        self.jenis = jenis
        self.merek = merek
        self.warna = warna
    def berkendara(self):
            print("kendaraan ini sedang berjalan")

class SepedaMotor(kendaraan):
    def __init__(self, jenis, merek, warna, cc):
        super().__init__(jenis, merek, warna)
        self.cc = cc

    def belok(self):
        print("Sepeda Motor ini sedang berjalan")

motorA = SepedaMotor("Sepeda Motor", "Honda", "Merah", 150)
motorA.berkendara() # output : kendaraan ini sedang berjalan
motorA.belok() # output : sepeda motor ini sedang belok.
