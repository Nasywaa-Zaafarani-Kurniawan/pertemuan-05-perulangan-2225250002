nilai = float(input("Masukkan nilai: "))
if nilai < 0 or nilai > 100:
    print("Nilai tidak valid. Masukkan nilai antara 0 dan 100.")
    nilai = float(input("Masukkan nilai 0-100: "))
print(f"Nilai yang dimasukkan: {nilai}")