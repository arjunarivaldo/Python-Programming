# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah satu class Mobil yang bisa digunakan untuk mencetak beragam tipe mobil
# Pastikan class tersebut memiliki setidaknya 3 attributes dan 3 methods

class Mobil:
    def __init__(self, jenis, warna, harga):
        self.jenis = jenis
        self.warna = warna
        self.harga = harga

    def beli(self):
        print(f'Saya ingin membeli Mobil dengan jenis {self.jenis}, warna {self.warna}, dengan harga {self.harga}.')

    def jual(self):
        print(f'Saya ingin menjual Mobil dengan jenis {self.jenis}, warna {self.warna}, dengan harga {self.harga}.')

    def cari(self):
        print(f'Saya sedang mencari Mobil dengan jenis {self.jenis}, warna {self.warna}, dan harga kisaran {self.harga}')

# mobil1 = Mobil(jenis = 'Merci', warna = 'Merah', harga = '100 Jt')
# mobil2 = Mobil(jenis = 'McLaren', warna = 'Ungu', harga = '5 Milyar')
#
#
# mobil2.cari()