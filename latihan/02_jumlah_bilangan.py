n = int(input("n: "))
total = 0
for i in range(n):
    bilangan = int(input(f"Masukkan bilangan ke-{i+1}: "))
    total += bilangan
print(f"Jumlah semua bilangan: {total}")