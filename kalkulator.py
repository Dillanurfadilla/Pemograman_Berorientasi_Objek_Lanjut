class kalkulator:
    @staticmethod 
    def add(x, y): 
        return x + y 
 
    @staticmethod 
    def subtract(x, y): 
        return x - y 
 
    @staticmethod 
    def multiply(x, y): 
        return x * y 
 
    @staticmethod 
    def divide(x, y): 
        if y == 0: 
             raise ValueError('Tidak dapat membagi dengan nol.') 
        return x / y

# Memanggil metode statis add() dan subtract() di dalam class Math 
print(kalkulator.add(3, 5)) # Output: 8 
print(kalkulator.subtract(10, 7)) # Output: 3 
 
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(kalkulator.multiply(4, 6)) # Output: 24 
print(kalkulator.divide(12, 4)) # Output: 3.0