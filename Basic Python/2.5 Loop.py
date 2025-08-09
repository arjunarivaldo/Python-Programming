# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# LOOP
#------------------------------

# While loop
count = 0
while (count < 9):
   print ("Nilai count: ", count)
   count = count + 1

print("Selamat tinggal!")

list_angka = [1,2,3,4,5] 

# For loop
for y in list_angka:
   print(y)

print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))

for x in list(range(1, 11)):
   print(x)

# Nested loop
i = 200

while (i < 100):
   j = 2
   print((i/j))
   while (j <= (i/j)):
      print("Loop dalam loop!")
      j = j + 1
      i = i + 1

print("Selamat tinggal!")

# Break & Continue
for val in "string":
   if val == "i":
      break

   print(val)

print("Loop telah berakhir.")

for val in "string":
   if val == "i":
      continue

   print(val)

print("Loop telah berakhir.")

# BONUS: FOR ELSE
daftar_murid = ['Angga', 'Mardadi', 'Rowi']

nama_murid = 'Farhan'

for nama in daftar_murid:
   if nama == nama_murid:
      print(nama)
      break
else:
   print("Nama murid tidak ditemukan.")

# BONUS: Pass
for nama in daftar_murid:
   pass
