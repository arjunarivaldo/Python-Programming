# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# CLASS
#------------------------------

class Cat:
    '''
    Ini adalah Class untuk membuat objek kucing
    Melalui kelas ini kita bisa mendefinisikan nama dan juga tipe dari kucing yang dibuat
    '''

    spesies = "Kucing"

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self, speed):
        print(f"Kucing {self.nama} berlari dengan {speed}...")

    def play(self):
        print(f"Kucing {self.nama} bermain dengan kucing lainnya...")

    def eat(self):
        pass

# Membuat objek
kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(f"Kinako adalah seekor {kinako.__class__.spesies}")
print(f"Minto adalah seekor {minto.__class__.spesies}")

print(f"{kinako.nama} merupakan kucing jenis {kinako.type}")
print(f"{minto.nama} merupakan kucing jenis {minto.type}")

kinako.run('cepat')
kinako.play()

print(kinako.__doc__)

del kinako.tipe

print(kinako)
print(kinako.tipe)

del kinako

print(kinako)

class Employee():
    '''
    Ini adalah Class untuk memanipulasi data employee
    Melalui kelas ini kita bisa memanipulasi data yang ada seperti baca, hapus dan tambah
    '''

    def __init__(self, lokasi_file):

        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca_data(self):

        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus_data(self, baris, kolom):

        del self.data_employee[baris][kolom]

    def tambah_data(self, data_baru):

        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])

# Membuat objek
it = Employee(lokasi_file='./karyawan_IT.xls')
marketing = Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')

# Abstract Object
class RandomForest():
    pass