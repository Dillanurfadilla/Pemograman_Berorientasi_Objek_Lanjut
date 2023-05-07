try:
    data = int(input("Masukkan angka awal :"))
    pembagi = data / int(input("Masukkan angka perkalian :"))
except ZeroDivisionError:
    print("Terjadi kesalahan, perkalian tidak boleh nol!")