# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# VARIABLE & DATA TYPE
#------------------------------

angka = 10
angka = 100
angka = 0.1

print(angka)

email = "contact@aiforindonesia.org"
print(email)

email = "angga@aiforindonesia.org"
print(email)

angka1, angka2, email = 10, 0.1, "contact@aiforindonesia.org"
print(angka1)
print(angka2)
print(email)

angka1 = angka2 = angka3 = 100
print(angka1)
print(angka2)
print(angka3)

# Constanta
PI = 3.14
GRAVITY = 9.8

# Naming
nama_variable = "Indonesia AI"
NAMA_VARIABLE = "Indonesia AI"
namaVariable = "Indonesia AI"
NamaVariable = "Indonesia AI"
# Dilarang: !, @, #, $, % dan digit 0-9 di awal

# Literals
nomor_biner = 0b1010 # Binary Literal
nomor_desimal = 100 # Decimal Literal 
nomor_float = 1.5e2 # Float Literal

print(nomor_biner)
print(nomor_desimal)
print(nomor_float)

#------------------------------
# DATA TYPE
#------------------------------

# Integer & Float
a = 5
print(a, "merupakan tipe data", type(a))

b = 2.0
print(b, "merupakan tipe data", type(a))

c = 4/5
print(c, "merupakan tipe data", type(c))

c = a + b
print(c, "merupakan tipe data", type(c))

c = int(c)
print(c, "merupakan tipe data", type(c))

a = float(5)
print(a, "merupakan tipe data", type(a))

a = str(5)
print(a, "merupakan tipe data", type(a))

c = 8/5
c = c.__ceil__()
print(c)

c = 8/5
c = c.__floor__()
print(c)

# String

s = "Ini adalah string single-line"

print(s, "merupakan tipe data", type(s))

s = '''Ini adalah string
namun bukan single-line melainkan multi-line'''

print(s)

s = "Ini adalah string single-line"
s = s.lower()
print(s)

s = s.upper()
print(s)

s = s.replace('ADALAH', 'MERUPAKAN')
print(s)

nama = "Angga"
s = f"Nama saya adalah {nama}"
s = "Nama saya adalah {}".format(nama)
print(s)

# Boolean
b = True
print(b, "merupakan tipe data", type(b))

print(b == 1)
print(b == 0)
print(not b)

# Boolean 'and' logic
# True and True = True
# False and True = False
# True and False = False
# False and False = False
print(True and True)
print(False and True)

print(True & True)
print(False & True)

# Boolean 'or' logic
# True or True = True
# False or True = True
# True or False = True
# False or False = False
print(True or True)
print(False or True)

print(True | True)
print(False | True)

# List, Tuple & Dictionary
l = [1, 2.2, 'python']
print(l, "merupakan tipe data", type(l))

t = (5,'program', 1+3)
print(t, "merupakan tipe data", type(t))

d = {'key1': 'value1', 'key2': 'value2'}
print(d, "merupakan tipe data", type(d))