# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop

dict_murid = {0: 'Ajeng',
              1: "Bambang",
              2: 'Cinta',
              3: 'Dani',
              4: 'Eri',
              5: 'Fitri',
              6: 'Galang',
              7: 'Heni',
              8: 'Ita',
              9: 'Joni'
}
dict_karyawan = {0:'aldo',
                 1: 'bambang',
                 2: 'cucun',
                 3: 'dea',
                 4: 'eti',
                 5: 'fuad',
                 6: 'gugun',
                 7: 'hendra',
                 8: 'ijang',
                 9: 'jeni'}

print('Nama murid di index ke-3 adalah: ', dict_murid[2])
print('Nama murid di index ke-9 adalah: ', dict_murid[9])
print('Nama karyawan di index ke-3 adalah: ',dict_karyawan[2])
print('Nama karyawan di index ke-9 adalah: ',dict_karyawan[9])

print('''
Di bawah ini adalah daftar nama murid
''')
for key, value in dict_murid.items():
    print (f"Indeks ke- {key}: {value}")

print('''
Di bawah ini adalah daftar nama karyawan
''')

for key, value in dict_karyawan.items():
    print(f"Indeks ke-{key}: {value}")