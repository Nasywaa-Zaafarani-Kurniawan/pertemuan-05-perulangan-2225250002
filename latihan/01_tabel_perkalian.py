n = int(input("Masukkan angka untuk tabel perkalian: "))
a = int(input("Masukkan batas angka pertama: "))
b = int(input("Masukkan batas angka terakhir: "))
for i in range(a, b + 1):
    print(f"{n} x {i} = {n * i}")