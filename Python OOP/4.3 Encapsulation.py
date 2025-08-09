# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# ENCAPSULATION
#------------------------------

class Mobil:
    def __init__(self, plat):

        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin= 40 # liter            

    # getter
    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin} liter")

    # setter
    def aturMaksimumBensin(self, bensin): 
        self.__bensin = bensin

avanza = Mobil(plat="B 7185 XC")
avanza.lihatMaksimumBensin()

avanza.__bensin = 100
avanza.lihatMaksimumBensin()

avanza.aturMaksimumBensin(200) # setter
avanza.lihatMaksimumBensin() # getter
