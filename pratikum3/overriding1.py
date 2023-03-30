class Animal:
    def add(self, Dog):
        return Dog
    def add(self, Cat):
        return Cat
    def add(self, Cihuahua):
        return Cihuahua
    def add(self, Siames):
        return Siames


Anl = Animal()
B = Anl.add("The Dog Barks")
print(B)
Anl = Animal()
C = Anl.add("The Cat Meows")
print(C)
Anl = Animal()
D = Anl.add("The cihuahua yaps")
print(D)
Anl = Animal()
E = Anl.add("The Siames purrs")
print(E)