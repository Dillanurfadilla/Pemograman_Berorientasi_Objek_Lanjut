print("\nNama: Dilla Nurfadilla")
print("\nNim: 210511086")
print("\nKelas: R2\n\n")

class DisneyHotstar:
    def __init__(self,Judul, Rilis):
        self.Judul= Judul
        self.Rilis = Rilis

class FlatFrom:
    def __init__(self,Nama, DisneyHotstar):
        self.Nama = Nama
        self.DisneyHotstar = DisneyHotstar

    def Kartun(self):
        print(f'\nFlatFrom\t:  {self.Nama}\n')
        for DisneyHotstar in self.DisneyHotstar:
            print(f'Judul\t\t: ',DisneyHotstar.Judul)
            print(f'Published\t:  {DisneyHotstar.Rilis}')
           
DisneyHotstar1 = DisneyHotstar('Frozen',   2013)
DisneyHotstar2 = DisneyHotstar('Turning_Red',   2022)
DisneyHotstar3 = DisneyHotstar('Zotopia', 2016)
FlatFrom1 = FlatFrom('DisneyHotstar', [DisneyHotstar1, DisneyHotstar2, DisneyHotstar3])
FlatFrom1.Kartun()
 