# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org
from debugpy.common.log import write

# Bacalah data yang ada di file data.txt
# Lalu tambahkan teks "Bahasa Pemrograman Python memiliki masa depan yang cerah"
# Pastikan tidak menghilangkan data yang sudah ada di file tersebut!

# with open("./data.txt", mode="a", encoding="utf-8") as data:
#     data.write("\nBahasa Pemograman Python memiliki masa depan yang cerah")

# with open ("./data.txt", mode='r', encoding="utf-8") as f:
#     baca = f.read()
#     print(baca)

# with open ('./data.txt', mode='a', encoding='utf-8') as f:
#     f.write('\nPython adalah bahasa pemograman yang mantap')

# with open ('./data.txt', mode='r', encoding='utf-8') as f:
#      baca = f.read()
#      baca = baca.replace('Python', 'PYTHON')
#      print(baca)

with open('./data.txt', mode='a', encoding='utf-8') as f:
     f.write('\nBelajar file handling sangat penting untuk data processing.')
