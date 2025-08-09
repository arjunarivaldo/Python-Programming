# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# ERROR HANDLING
#------------------------------

# Syntax error
fruit_list = ["apple", "banana", "watermelon"]
# for fruit in fruit_list
# SyntaxError: invalid syntax

# Logical error
nilai = 10
pembagi = 0
# hasil = nilai/pembagi
# ZeroDivisionError: division by zero

print(dir(locals()['__builtins__']))

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except:
    print("Oops! Terjadi error.")

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except Exception as e:
    print("Oops! Terjadi ", e.__class__, ".")

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except ZeroDivisionError:
    print("Oops! Terjadi ZeroDivisionError.")
except ValueError:
    print("Oops! Terjadi ValueError.")
except:
    print("Oops! Terjadi error yang tidak dikenali.")


try:
    nilai = 10
    pembagi = 2
    hasil = nilai/pembagi
except Exception as e:
    print("Oops! Terjadi ", e.__class__, ".")
else:
    print("Tidak ada error.")


class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

number = 10

while True:
    try:
        i_num = int(input("Masukan angka: "))

        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    
    except ValueTooSmallError:
        print("Angka yang kamu tebak terlalu kecil, coba lagi!")
        print()
    except ValueTooLargeError:
        print("Angka yang kamu tebak terlalu besar, coba lagi!")
        print()

print("Betul! Kamu berhasil menebak dengan tepat.")