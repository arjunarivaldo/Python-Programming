# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# POLIMORPHISM
#------------------------------

# Class
class Cat:
    def __init__(self):
        self.nama = "Meong"
        self.tipe = "Anggora"

    def forward(self):
        print("Kucing berlari...")

# Class
class Bird:
    def __init__(self):
        self.nama = "Erago"
        self.tipe = "Elang"

    def forward(self):
        print("Burung terbang...")

def melaju(objek):
    objek.forward()

meong = Cat(); erago = Bird()

melaju(meong)
melaju(erago)