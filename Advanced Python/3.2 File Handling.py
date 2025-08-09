# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# FILE HANDLING
#------------------------------

# Ini adalah file data.txt
# Pada file ini memuat beberapa informasi tentang data
# Data ini akan diproses menggunakan python

# Read
data = open('./data.txt', mode='r')
print(data.read(5))
print(data.read()) # Latihan dasar menangani file di python

data = open('./data.txt', mode='r', encoding='utf-8') # recommended 
print(data.read()) # Latihan dasar menangani file di python

string = data.read()
string = string.replace('adalah', 'merupakan')
print(string)

# Append
data = open('./data.txt', mode='a')
data.write("\nYuk belajar bahasa pemrograman Python!")
data.write("\nAgar jago harus sering berlatih!")
data.close()

# Write
data = open('./data.txt', mode='w')
data.write("\nYuk belajar bahasa pemrograman Python!")
data.write("\nAgar jago harus sering berlatih!")
data.close()

# Better practice
try:
   f = open('./data.txt', mode='w', encoding='utf-8')
finally:
   f.close()

# Best practice
with open('./data.txt', mode='w', encoding='utf-8') as f:
    pass