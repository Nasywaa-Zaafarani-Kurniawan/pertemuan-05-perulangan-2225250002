# pertemuan-05-perulangan-2225250002

## Identitas
* **Nama**: Nasywaa Zaafarani Kurniawan
* **NIM**: 2225250002
* **Kelas**: 3A

---

## Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas praktikum Pertemuan 5 mata kuliah Algoritma dan Pemrograman. Repositori ini berisi latihan dan praktik penggunaan struktur perulangan (*loops*), baik menggunakan `for` maupun `while`, untuk menyelesaikan masalah iteratif, membangun deret aritmetika, serta mengelola proses perhitungan berulang secara terstruktur pada Python.

---

## Daftar dan Fungsi Berkas

### Folder `latihan/`
*(Dapat diisi dengan skrip latihan perulangan terkait seperti penggunaan `for`, `while`, `break`, `continue`, atau akumulasi nilai iteratif).*

### Folder `kuis/` atau `praktik/`
* **`kuis2_deret_aritmetika.py`**: Program utama untuk menghasilkan deret aritmetika berdasarkan nilai suku awal (a), beda (d), dan jumlah suku (n), serta menghitung total jumlah keseluruhan suku dalam deret tersebut.

---

## Algoritma Kuis 2
Langkah-langkah perulangan dan logika program disusun sebagai berikut:
1. Menerima masukan dari pengguna berupa nilai awal (a), beda (d), dan jumlah suku (n).
2. Menggunakan struktur perulangan (`for` atau `while`) sebanyak n kali iterasi.
3. Pada setiap iterasi, nilai suku saat ini dihitung dengan rumus aritmetika dasar, lalu disimpan atau dicetak sebagai bagian dari deret suku.
4. Menambahkan nilai suku tersebut ke dalam variabel akumulator (jumlah total) pada setiap langkah perulangan.
5. Menampilkan seluruh deret suku yang terbentuk beserta hasil akhir penjumlahan seluruh suku tersebut.

---

## Hasil Pengujian Kuis 2 (`kuis/kuis2_deret_aritmetika.py`)

| a | d | n | Keluaran yang Diharapkan (Suku) | Keluaran yang Diharapkan (Jumlah) | Status |
| :-: | :-: | :-: | :--- | :--- | :-: |
| 2 | 3 | 5 | 2, 5, 8, 11, 14 | 40 | Sesuai |
| 10 | -2 | 4 | 10, 8, 6, 4 | 28 | Sesuai |
| 1.5 | 0.5 | 3 | 1.5, 2.0, 2.5 | 6.0 | Sesuai |

---

## Cara Menjalankan
Buka terminal di direktori utama repositori ini, lalu jalankan program menggunakan perintah berikut:

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

---

## Refleksi
Dalam praktikum Pertemuan 5 ini, saya mempelajari cara mengimplementasikan struktur perulangan (loops) di Python untuk menangani proses iterasi dan perhitungan akumulatif secara otomatis.Hal yang paling saya pahami adalah bagaimana menentukan batas perulangan menggunakan nilai n dan menggeser nilai suku secara dinamis berdasarkan selisih atau beda (d). Kendala yang sempat saya hadapi adalah mengatur format penulisan cetak deret suku agar tanda pemisah koma antar suku muncul dengan rapi tanpa kelebihan koma di akhir baris, serta menginisialisasi variabel penjumlahan (accumulator) dengan nilai awal yang tepat agar hasil totalnya tidak keliru. Masalah ini berhasil saya atasi dengan menyusun logika penampung deret (menggunakan list atau string builder) dan memastikan variabel jumlah diatur mulai dari angka nol sebelum perulangan dimulai.
