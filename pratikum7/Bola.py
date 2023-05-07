print("\nDilla Nurfadilla 210511086 R2\n\n")

class BolaMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, jari):
            return 4 * 3.14 * jari * jari
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari):
            return 4/3 * 3.14 * jari * jari * jari
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=BolaMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(18)
C = A.volume(9)
print('Luas Permukaan Bola:',B)
print('Volume Bola:',C)