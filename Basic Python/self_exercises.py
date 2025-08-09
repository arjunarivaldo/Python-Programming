# for i in range (1,11):
#     print (i, end=' ')

# bintang = '*' 
# for i in bintang:
#     print (i, end=' ')
#     bintang

# for _ in range (6):
#     print ('*', end=' ')

# for i in range (1,6):
#     print ([i], end='')

# for i in range (1,6):
#     for j in range (1, i+1):
#         print(j, end='')
#     print()

# for i in range (5,0,-1):
#     for j in range (1, i+1):
#         print(j, end='')
#     print()

# for i in range (1,6):
#     for _ in range (5-i):
#         print (' ', end='')
#     for j in range (1, i+1):
#         print (j, end='')
#     print()    

# Jawaban pola 2
# for i in range (0,5):
#     for _ in range (0+i):
#         print(' ', end='')
#     for j in range (1, 6-i):
#         print(j, end="")
#     print()

# Jawaban pola 3
# for i in range (0,5):
#     for _ in range (5,0+i,-1):
#         print(' ',end='')
#     for j in range (1,2+i):
#         print(j, end=' ')
#     print()

# Jawaban pola 4
# for i in range (5):
#     for _ in range(4,0+i,-1):
#         print(' ', end="")
#     for j in range(i, i+1):
#         print(f'{j} ', end='  ')
#     print()


# for i in range (1, 6):
#     print (' ' * (5-i), end='')
#     for j in range (i):
#         print (f'{i} ', end='')
#     print()


#Jawaban pola 5
# list = [1]
# list2 = [2]
# for i in range (1,6):
#     for j in list:
#         print (j, end=' ')
#     list.append(list + list2)
#     print()
# Level 1

#No1
def greet():
    print("Hello, world!")
    
greet()

#No2
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

#No3
def add(a, b):
    return a + b

hasil = add(10, 20)
print(hasil)

#No4
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

is_even_result = is_even(10)
print(is_even_result)

#No5
def square(n):
    return n * n

square_result = square(5)
print(square_result)

    