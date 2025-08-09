# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# FUNCTION
#------------------------------

# Non parameter
def halo_dunia():
    var = 'Halo Python, halo dunia!'
    print(var)

halo_dunia()

# Parameter
def selamat_datang(nama):
    var = f'Halo {nama}, welcome!'
    print(var)

selamat_datang('nurul')

def selamat_datang(nama, asal):
    var = f'Halo {nama} dari {asal}, welcome!'
    print(var)

selamat_datang('nurul', 'Purwokerto')
selamat_datang(nama = 'nurul', asal = 'Purwokerto')

def selamat_datang(*daftar_nama):

    var = 'Halo '
    for nama in daftar_nama:
        var += nama + ', '

    var += 'welcome!'
    print(var)

selamat_datang('nurul', 'Siska', 'Lukman')

# Anonim
double = lambda x: x * 2

print(double(5))

# BONUS: Docstring
def selamat_datang(nama):
    '''
    Ini adalah fungsi untuk menyapa
    nama yang telah disebutkan
    '''
    var = f'Halo {nama}, welcome!'
    print(var)

selamat_datang('nurul')

print(selamat_datang.__doc__)

# BONUS: Scope & Return
a = 2
b = 1

x = 100

a = 2
b = 1

x = 100

def operasi(a, b, c=1):

    op1 = a + b
    op2 = op1 // c

    print('a di dalam function:', a)
    print('b di dalam function:', b)

    print(x)

    return op2

hasil = operasi(a=10, b=5, c=3)
print(hasil)

print('a di luar function:', a)
print('b di luar function:', b)

# print(op2)