# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org
#from test.test_pipes import pipes


# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki fungsi setter & getter
# Pastikan fungsi tersebut memungkinkan kita untuk memodifikasi semua attributes yang dimiliki oleh class tersebut

class Mobil:
    def __init__(self, jenis, warna, harga):
        self.jenis = jenis
        self.warna = warna
        self.harga = harga
        self.__bensin= 40 #liter
        self.__jarak = 500 #km

    def beli(self):
        print(f'Saya ingin membeli Mobil dengan jenis {self.jenis}, warna {self.warna}, dengan harga {self.harga}.')

    def jual(self):
        print(f'Saya ingin menjual Mobil dengan jenis {self.jenis}, warna {self.warna}, dengan harga {self.harga}.')

    def cari(self):
        print(f'Saya sedang mencari Mobil dengan jenis {self.jenis}, warna {self.warna}, dan harga kisaran {self.harga}')

    #Getter
    def LihatMaksimumBensin(self):
        print(f'Maksimum bensin adalah {self.__bensin}')

    #Setter
    def AturMaksimumBensin(self, bensin):
        self.__bensin = bensin


# mobil1 = Mobil(jenis = 'Merci', warna = 'Merah', harga = '100 Jt')
# mobil2 = Mobil(jenis = 'McLaren', warna = 'Ungu', harga = '5 Milyar')
#
#
# mobil2.cari()

# Tambahkan setter & getter

McLaren = Mobil(jenis= "McLaren", warna= 'Ungu', harga='5M')

McLaren.LihatMaksimumBensin()

McLaren.AturMaksimumBensin(100)
McLaren.LihatMaksimumBensin()