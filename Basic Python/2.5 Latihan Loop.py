# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah operasi loop yang akan mencetak angka GENAP dari 1-120
# Lalu gunakan statement continue agar operasi tidak mencetak angka 12, 56 dan 78
# Dan juga gunakan statement break agar operasi berhenti hanya sampai di angka 100


list_angka = list(range(2, 121, 2))

for x in list_angka:
    if x == 12 or x == 56 or x == 78:
        continue
    elif x == 102:
        break
    print(x)

from IPython.terminal.shortcuts.filters import pass_through

#Dibawah ini adalah latihan yang saya buat sendiri, supaya lebih memahami materi Loop ini.

'''
🔁 Latihan 1: Cetak Angka Ganjil (For Loop + If)
Cetak semua angka ganjil dari 1 sampai 20 menggunakan for loop.

💡 Hint: Gunakan if x % 2 != 0

🔁 Latihan 2: Jumlahkan Semua Angka dalam List
Buat sebuah list angka dan jumlahkan semua elemennya menggunakan for loop.
Contoh list: [3, 5, 7, 2, 8]

🔁 Latihan 3: Cari Angka di Dalam List (For-Else)
Buat program untuk mencari angka tertentu di dalam sebuah list.
Jika angka ditemukan, cetak "Ditemukan!" dan hentikan loop.
Kalau tidak, tampilkan "Tidak ditemukan".

🔁 Latihan 4: Skip Angka Tertentu (Continue)
Cetak semua angka dari 1 sampai 10, kecuali angka 4 dan 7.

🔁 Latihan 5: Tampilkan Pola Bintang (Nested Loop)
Tampilkan pola berikut menggunakan nested loop:

*
**
***
****
*****

🔁 Latihan 6: While Loop Counter
Gunakan while loop untuk mencetak angka dari 10 ke 1 (mundur), lalu tampilkan "Selesai!".

🔁 Latihan 7: Daftar Nama dan Huruf
Berikan list nama seperti ["Ayu", "Budi"].
Cetak setiap huruf dari tiap nama satu per satu (gunakan nested for loop).

🔁 Latihan 8 (BONUS): Tebak Angka
Buat game tebak angka sederhana:

Angka rahasia adalah 7

Pengguna diminta menebak angka sampai benar

Gunakan while loop dan input()
'''


# Latihan 1: Cetak Angka Ganjil (For Loop + If)
'''Cetak semua angka ganjil dari 1 sampai 20 menggunakan for loop.

💡 Hint: Gunakan if x % 2 != 0
'''

'''for x in range(1,21):
    if x % 2 != 0:
        print(x)
# Atau bisa juga seperti ini, pilih yang mudah dibaca
for x in range(1, 21, 2):
    print (x)'''



# Latihan 2: Jumlahkan Semua Angka dalam List
'''Buat sebuah list angka dan jumlahkan semua elemennya menggunakan for loop.
Contoh list: [3, 5, 7, 2, 8]
'''
'''
list = [3, 2, 4, 6, 8, 2, 8, 9]
total = 0

for x in list:
    total = total + x

print ('Jumlah total yang ada di list adalah: ', total'''

# Latihan 3: Cari Angka di Dalam List (For-Else)
'''Buat program untuk mencari angka tertentu di dalam sebuah list.
Jika angka ditemukan, cetak "Ditemukan!" dan hentikan loop.
Kalau tidak, tampilkan "Tidak ditemukan".'''

'''angka = [2,31,54,76,35,96,35,12,34,6,78,3,1,9,0,56,87,24,87,92,85,36,10]
tebakan = float(input("Masukan angka: "))

for x in angka:
    if tebakan == x:
        print("Angka ditemukan!")
        break
else:
    print('Angka tidak ditemukan!')'''

#Latihan 3 variasi lain yang mirip
'''
Buat program yang meminta pengguna mengetik satu huruf, lalu periksa apakah huruf itu ada di dalam kalimat yang sudah disediakan.

Jika ada:

Cetak: "Huruf ditemukan!" dan hentikan loop.

Jika tidak ada:

Setelah loop selesai, cetak: "Huruf tidak ditemukan."
'''
'''kalimat = "Python itu seru sekali bro!".lower()
tebakan_huruf = str(input("Ketikan satu huruf: ")).lower()

for x in kalimat:
    if tebakan_huruf == x:
        print ("Tebakan anda benar!")
        break
else:
    print("Tebakan anda salah!")'''

#🔁 Latihan 4: Skip Angka Tertentu (Continue)
'''Cetak semua angka dari 1 sampai 10, kecuali angka 4 dan 7.'''
'''angka = range(1, 11)

 x in angka:
    if x == 4:
        continue
    elif x == 7:
        continue
    print(x)

# Atau jika ingin lebih ringkas bisa gunakan

for x in angka:
    if x == 4 or x == 7:
        continue
    print(x)'''

# Latihan 5: Tampilkan Pola Bintang (Nested Loop)
'''Tampilkan pola berikut menggunakan nested loop:

*
**
***
****
*****'''