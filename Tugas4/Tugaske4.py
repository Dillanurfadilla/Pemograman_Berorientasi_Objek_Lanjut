print("\nNama: Dilla Nurfadilla")
print("\nNim: 210511086")
print("\nKelas: R2\n\n")

class idol:
    def __init__(self,Name_idol,Debut):
        self.Name_idol = Name_idol
        self.Debut = Debut

class Agensi:
    def __init__(self,Name_Agensi, idol):
        self.Name_Agensi = Name_Agensi
        self.idol = idol

    def daftar_idol(self):
        print(f'\nAgensi\t:  {self.Name_Agensi}\n')
        for idol in self.idol:
            print(f'Name_idol\t\t: ',idol.Name_idol)
            print(f'Published\t:  {idol.Debut}')
           
idol1 = idol('BTS',   2013)
idol2 = idol('TXT',   2018)
Agensi1 = Agensi('HYBE', [idol1, idol2])
Agensi1.daftar_idol()
 