print("\nDilla Nurfadilla 210511086 R2\n\n")

class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, jari, tinggi):
            return 2 * 22/7 * jari * (jari + tinggi)
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari, tinggi):
            return 22/7 * jari * jari * tinggi
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=TabungMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(32, 23)
C = A.volume(26, 23)
print('Luas Permukaan Tabung:',B)
print('Volume Tabung:',C)