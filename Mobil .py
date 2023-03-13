class Mobil:
   def __init__(self, merk, warna):
       self.merk = merk
       self.warna = warna
   def info(self):
    print(f"Mobil {self.merk} berwana {self.warna}")
MobilA = Mobil("Toyota", "Hitam")
MobilA.info() # Output: Mobil Toyota berwarna hitam