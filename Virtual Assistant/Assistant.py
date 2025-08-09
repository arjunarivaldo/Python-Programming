import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Assistant():

    def __init__(self, name):
        
        self.name = name
        
    def kirim_email():
        pengirim = input("Masukkan alamat email kamu: ")
        penerima = input("Masukkan alamat email tujuan: ")
        sandi_app = '' #Masukan sandi app
        subjek = input("Masukkan subjek email: ")
        isi = input ('Masukkan isi email: ')
        
        pesan = MIMEMultipart()
        pesan['From'] = pengirim
        pesan['To'] = penerima
        pesan['Subject'] = subjek  
        pesan.attach(MIMEText(isi, 'plain'))
        
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(pengirim, sandi_app)
            server.send_message(pesan)
            server.quit()
        
            print("\nEmail berhasil dikirim!")
        
        except smtplib.SMTPAuthenticationError:
            print ("❌ Login gagal: Cek email dan app password kamu.")
            
        except smtplib.SMTPConnectError:
            print("❌ Gagal terhubung ke server SMTP. Periksa koneksi internet kamu.")
        
        except Exception as e:
            print(f"❌ Terjadi kesalahan: {e}")
            
    def tambah_jadwal():
        tanggal = input ('Masukan tanggal (DD-MM-YYYY): ')
        waktu = input ('Masukan waktu (HH:MM): ')
        kegiatan = input ('Masukan kegiatan: ')
        
        data = f"{tanggal} | {waktu} | {kegiatan}\n"
        
        try:
            with open('jadwal.txt', 'a') as file:
                file.write(data)
            print("\n✅Jadwal berhasil ditambahkan!")
        except Exception as e:
            print(f"❌ Terjadi kesalahan saat menambahkan jadwal: {e}")
        
    def lihat_jadwal():
        try:
            with open('jadwal.txt', 'r') as file:
                jadwal = file.readlines()
                if not jadwal:
                    print("\n📅 Tidak ada jadwal yang tersimpan.")
                else:
                    print("\n📅 Jadwal Anda:")
                    for item in jadwal:
                        print(item.strip())
        except FileNotFoundError:
            print("\n📅 File jadwal tidak ditemukan. Silakan tambahkan jadwal terlebih dahulu.")
        except Exception as e:
            print(f"❌ Terjadi kesalahan saat membaca jadwal: {e}")
            
    def edit_jadwal():
        try:
            with open("jadwal.txt", "r") as file:
                jadwal = file.readlines()

            if not jadwal:
                print("Belum ada jadwal untuk diedit.")
                return

            print("\n📋 Daftar Jadwal:")
            for i, item in enumerate(jadwal, 1):
                print(f"{i}. {item.strip()}")

            nomor = int(input("Pilih nomor jadwal yang mau diedit: "))
            if 1 <= nomor <= len(jadwal):
                tanggal = input("Tanggal baru (dd-mm-yyyy): ")
                waktu = input("Waktu baru (HH:MM): ")
                kegiatan = input("Kegiatan baru: ")

                jadwal[nomor - 1] = f"{tanggal} | {waktu} | {kegiatan}\n"

                with open("jadwal.txt", "w") as file:
                    file.writelines(jadwal)

                print("✅ Jadwal berhasil diedit.")
            else:
                print("❌ Nomor tidak valid.")

        except FileNotFoundError:
            print("❌ File jadwal tidak ditemukan.")

    def hapus_jadwal():
        try:
            with open("jadwal.txt", "r") as file:
                jadwal = file.readlines()

            if not jadwal:
                print("Belum ada jadwal untuk dihapus.")
                return

            print("\n🗂️ Daftar Jadwal:")
            for i, item in enumerate(jadwal, 1):
                print(f"{i}. {item.strip()}")

            nomor = int(input("Pilih nomor jadwal yang mau dihapus: "))
            if 1 <= nomor <= len(jadwal):
                hapus = jadwal.pop(nomor - 1)

                with open("jadwal.txt", "w") as file:
                    file.writelines(jadwal)

                print(f"✅ Jadwal '{hapus.strip()}' berhasil dihapus.")
            else:
                print("❌ Nomor tidak valid.")

        except FileNotFoundError:
            print("❌ File jadwal tidak ditemukan.")

    def jokes():
        jokes_list = [
            "Kenapa komputer tidak bisa berlari? Karena dia selalu crash!",
            "Mengapa programmer suka minum kopi? Karena mereka butuh Java!",
            "Apa yang dikatakan satu dinding ke dinding lainnya? Kita akan bertemu di sudut!",
            "Mengapa matematika sangat sedih? Karena dia punya terlalu banyak masalah!",
            "Apa yang dilakukan programmer saat lapar? Dia makan byte!"
        ]
        print (random.choice(jokes_list))
        

    def menu(self):
        while True:
            try:
                print(f'\n========= {self.name} Virtual Assistant =========')
                print('1. Kirim Email')
                print('2. Tambah Jadwal')
                print('3. Lihat Jadwal')
                print('4. Edit Jadwal')
                print('5. Hapus Jadwal')
                print('6. Dapatkan Joke')
                print('7. Keluar')
                choice = int(input('Pilih menu: '))
                
                if choice == 1:
                    Assistant.kirim_email()
                elif choice == 2:
                    Assistant.tambah_jadwal()
                elif choice == 3:
                    Assistant.lihat_jadwal()
                elif choice == 4:
                    Assistant.edit_jadwal()
                elif choice == 5:
                    Assistant.hapus_jadwal()
                elif choice == 6:
                    Assistant.jokes()
                elif choice == 7:
                    print(f'Terima kasih telah menggunakan {self.name} Virtual Assistant!')
                    break
                else:
                    print('Pilihan tidak valid, silakan coba lagi.')
            except ValueError:
                print('Input tidak valid, silakan masukkan angka.')