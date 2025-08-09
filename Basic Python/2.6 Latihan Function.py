# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah fungsi yang akan mengevaluasi apakah modulus dari hasil kali 2 angka yang diterima bernilai 0 atau tidak
# Gunakan statement return untuk mengembalikan nilai tersebut lalu cetak hasilnya
# Beri nama cek_modulus() pada fungsi tersebut

def cek_modulus(a,b):
    return (a*b) % 2 == 0

hasil = cek_modulus(4, 5)
print(hasil)

# from test.test_ctypes.test_pickling import proto
# from traceback import print_tb

# '''
# 🧪 Latihan 1: Luas Persegi Panjang
# Buat fungsi luas_persegi_panjang(panjang, lebar) yang menghitung dan mengembalikan (pakai return) luasnya.
# '''
# '''
# def luas_persegi_panjang(panjang, lebar ):
#     a = panjang * lebar
#     return a

# panjang = float(input('Masukan panjangnya: '))
# lebar = float(input('Masukan lebarnya: '))

# hasil = luas_persegi_panjang(panjang, lebar)

# print ("Luas persegi panjang adalah: ", hasil)
# '''
# '''
# 🧪 Latihan 2: Salam Banyak Orang
# Buat fungsi sapa_semua(*nama_orang) yang mencetak:
# Halo <nama1>, <nama2>, ..., selamat datang!
# Gunakan *args.
# '''
# # def sapa_semua(*nama_orang):

# #     var = 'Halo '
# #     for x in nama_orang:
# #         var += x + ','
# #     var += 'Selamat datang!'

# # sapa_semua('aldo', 'sigit', 'sugeng')


# '''
# 🧪 Latihan 3: Hitung Total dan Rata-rata
# Buat fungsi hitung_total_rata(*angka) yang menerima angka dalam jumlah tak terbatas, dan:

# Mengembalikan total dan rata-rata sebagai tuple

# Contoh:
# hitung_total_rata(10, 20, 30)
# # Output: (60, 20.0)

# 🧪 Latihan 4: Periksa Bilangan Genap
# Buat lambda function genap = lambda x: ... untuk memeriksa apakah sebuah angka genap.
# Gunakan dalam bentuk:

# print(genap(10))  # True
# print(genap(5))   # False

# 🧪 Latihan 5 (BONUS): Docstring
# Tulis fungsi dengan docstring dan tampilkan penjelasannya menggunakan:

# print(nama_fungsi.__doc__)

# 🧪 Latihan 6: Return dan Scope
# Buat fungsi kali_dan_tambah(a, b, k=1) yang:

# Mengalikan a dan b

# Menambahkan k

# Kembalikan hasilnya
# Tampilkan nilai variabel luar dan dalam untuk melihat perbedaan scope.
# '''

# '''
# Latihan *args
# '''

# # def daftar_tamu (*nama_tamu):
# #     print(nama_tamu)
# # daftar_tamu("Aldo", 'sigit', 'sugeng')
# #
# # def penjumlahan (*angka):
# #     total = 0
# #     for x in angka:
# #         total += x
# #
# #     return total

# # def sapa_semua (*nama):
# #     for x in nama:
# #         print(f"Halo, {x}!")
# #
# # sapa_semua("Aldo", "Umay", "Dodol")

# # def penjumlahan (*angka):
# #     total = 0
# #     for x in angka:
# #         total += x
# #
# #     return total
# #
# # print(penjumlahan(2,4,56))
# # print(penjumlahan(5,1,4))
# # print(penjumlahan())

