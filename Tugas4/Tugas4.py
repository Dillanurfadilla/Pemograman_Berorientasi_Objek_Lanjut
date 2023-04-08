print("\nNama: Dilla Nurfadilla")
print("\nNim: 210511086")
print("\nKelas: R2\n\n")

class Lagu:
    def __init__(self,Judul, Genre,):
        self.Judul = Judul
        self.Genre = Genre
        
class Penyanyi:
    def __init__(self,Nama, Lagu):
        self.Nama = Nama
        self.Lagu = Lagu

    def Musik(self):
        print(f'\nPenyanyi\t:  {self.Nama}\n')
        for Lagu in self.Lagu:
            print(f'Judul\t\t: ',Lagu.Judul)
            print(f'Genre\t\t:  {Lagu.Genre}')
    
Lagu1 = Lagu('Shinunoga_E_Wa', 'Pop')
Lagu2 = Lagu('Kirari', 'Pop')
Lagu3 = Lagu('Matsuri', 'Pop')
Penyanyi1 = Penyanyi('Fuji_Kaze', [Lagu1, Lagu2, Lagu3])
Penyanyi1.Musik()
 