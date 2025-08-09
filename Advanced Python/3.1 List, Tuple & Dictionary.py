# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

#------------------------------
# LIST, TUPLE & DICTIONARY
#------------------------------

# List
print('''
    List
    ''')
list1 = ["apple", "banana",  "watermelon"]
list2 = [2, 1, 2, 7, 4, 10]
list3 = [True, False, False]
list4 = ["abc", 10, True, 40, "male"]

print(list1 + list2)

list2.sort()
print(list2)

list2.reverse()
print(list2)

list3 = list2.copy()
print(list3)

print(list3.count(2))

fruit_list = ["apple", "banana", "watermelon", "orange", "mango"]
fruit_list[1] # banana
fruit_list[1:4] # banana, watermelon, orange
fruit_list[-2:] # orange, mango

print(fruit_list)

fruit_list = ["apple", "banana", "watermelon", "orange", "mango"]
fruit_list[2] = "avocado"

# Membership test
print(fruit_list)
print('avocado' in fruit_list)
print('pineapple' not in fruit_list)

fruit_list = ["apple", "banana"]
fruit_list.append("watermelon") # "apple", "banana", "watermelon"

print(fruit_list)

fruit_list = ["apple", "banana", "watermelon"]
fruit_list.insert(1, "orange") # "apple", "orange", "banana", "watermelon"

print(fruit_list)

fruit_list1 = ["apple", "orange"]
fruit_list2 = ["banana", "watermelon"]
fruit_list1.extend(fruit_list2 ) # "apple", "orange", "banana", "watermelon"

print(fruit_list)

fruit_list = ["apple", "orange", "banana", "watermelon"]
fruit_list.remove("orange") # "apple", "banana", "watermelon"

print(fruit_list)

fruit_list = ["apple", "orange", "banana", "watermelon"]
fruit_list.pop(1) # "apple", "banana", "watermelon"

print(fruit_list)

fruit_list = ["apple", "orange", "banana", "watermelon"]
del fruit_list[1] # "apple", "banana", "watermelon"

print(fruit_list)

fruit_list.clear()

print(fruit_list)

# Tuple
print ('''
    Tuple
    ''')
tuple1 = ("apple", "banana",  "watermelon")
tuple2 = (1, 3, 7, 9, 10)
tuple3 = (True, False, False)
tuple4 = ("abc", 10, True, 40, "male")

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
fruit_tuple[1] # banana
fruit_tuple[1:4] # banana, watermelon, orange
fruit_tuple[-2:] # orange, mango

print(fruit_tuple)

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
# fruit_tuple[1] = "banana"

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
# del fruit_tuple[1]

for fruit in fruit_tuple:
    print("Nama buah:", fruit)

# Dictionary
print('''
    Dictionary
    ''')
fruit_dict = { 'nama': 'pisang', 
            'jenis': 'ambon', 
            'kode': 891, 
            'harga': 20000 }

print(fruit_dict['nama'])

fruit_dict['nama'] = 'jeruk'

print(fruit_dict['nama'])

fruit_dict['price'] = 3000

for key, value in fruit_dict.items():
    print(key, value)

for key in fruit_dict.keys():
    print(key, fruit_dict[key])

# BONUS: Set
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
print(A | B)

# Intersection
print(A & B)

# Difference
print(A - B)
print(B - A)

# Symmetric Difference
print(A ^ B)