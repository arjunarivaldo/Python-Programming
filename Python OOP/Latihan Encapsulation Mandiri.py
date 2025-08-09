# # Buat class UserLogin dengan atribut:
# # __username
# # __password
# #
# # Tambahkan method:
# # set_password(password_baru)
# # check_password(input_password)
# #
# # display_user()
#
# class UserLogin:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password
#
#     def set_password(self, password_baru):
#         if password_baru == self.__password:
#             print("Password sama dengan password lama, set password baru!")
#         else:
#             self.__password = password_baru
#             print('Password baru telah di set!')
#
#     def check_password(self, input_password):
#         if input_password == self.__password:
#             print("Password yang Anda masukkan benar!")
#             return True
#         else:
#             print("Password yang Anda masukkan salah!")
#             return False
#     # def check_password(self):
#     #     if input('Ketikan Password: ') == self.__password:
#     #         print('Password yang anda masukan benar!')
#     #     else:
#     #         print('Password yang anda masukan salah!')
#
#     def display_user(self):
#         print(f'Username: {self.__username}')
#
# login = UserLogin('arjunarivaldo', 'arjuna21')
# #
# # #login.check_password()
# #
# #login.set_password('arjuna21')
# #
# login.check_password("arjuna21")
# #login.display_user()


def tambah (a,b):
    hasil = a + b
    return hasil

x = tambah(5,5)

print(x)


