# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# CONDITION
#------------------------------
jumlah_penumpang = 3

# IF
if jumlah_penumpang > 10:
    print("Mobil berjalan")

if jumlah_penumpang < 10:
    print("Mobil menunggu penumpang lain")
print("Di luar condition")

print("Apakah 3 < 10:", 3 < 10)

score = 78

# IF ELIF
if score > 75:
    print('Lulus')
elif score < 10:
    print('Tidak lulus')

# IF ELIF ELSE
if score >= 85:
    print('Predikat A/Memuaskan')
elif score >= 75:
    print('Predikat B/Bagus')
else :
    print('Tidak Lulus')

kelas = 3

# NESTED IF
if kelas > 1:
    if score >= 85:
        print('Predikat A/Memuaskan')
    elif score >= 75:
        print('Predikat B/Bagus')
    else:
        print('Tidak Lulus')
else:
    if score >= 80:
        print('Predikat A/Bagus')
    else:
        print('Tidak Lulus')

num = float(input("Masukkan angka: "))
if num >= 0:
    if num == 0:
        print("Nol")
    else:
        print("Angka positif")
else:
    print("Angka negatif")