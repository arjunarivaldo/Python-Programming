# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah 2 variable yang memuat string
# Variable 1 memuat "Hello, "
# Variable 2 memuat "Python!"
# Lalu gabungkan kedua string tersebut dan tampung di variable hasil seperti ini
# hasil = variable1 + variable2
# Pastikan string yang ada bersifat upper-case
# Lalu cek apa Data Type dari variable hasil tersebut!

variable1 = "Hello, "
variable2 = "Python!"

hasil = variable1 + variable2
hasil = hasil.upper()

print (hasil)

print (hasil, "merupakan type jenis: ", type(hasil))

# Dibawah ini adalah latihan terpisah

variable = "Ini adalah string 1, dan ini adalah string 2"
print (variable)

variable = variable.replace("adalah", "merupakan")
variable = variable.replace ("dan", "lalu")
print (variable)

nama = 'Arjuna'
nama_lengkap = 'Arjuna Rivaldo Satria Prayoga'
v_nama = f'Nama saya adalah {nama} dan nama lengkap saya adalah {nama_lengkap}'

print(v_nama)