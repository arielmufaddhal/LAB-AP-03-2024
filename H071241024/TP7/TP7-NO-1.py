import os
import random
from datetime import datetime

FOLDER_FILM = "Films"
FILM_FILE = os.path.join(FOLDER_FILM, "daftar_film.txt")
FOLDER_TIKET = "Tickets"

daftar_film = []

def buat_struktur_folder():
    if not os.path.exists(FOLDER_FILM):
        os.makedirs(FOLDER_FILM)
    if not os.path.exists(FOLDER_TIKET):
        os.makedirs(FOLDER_TIKET)
    if not os.path.exists(FILM_FILE):
        open(FILM_FILE, 'w').close()

def muat_data():
    global daftar_film
    if os.path.exists(FILM_FILE):
        with open(FILM_FILE, 'r') as file:
            daftar_film = [line.strip() for line in file if line.strip()]

def simpan_film():
    with open(FILM_FILE, 'w') as file:
        for film in daftar_film:
            file.write(f"{film}\n")

def tambah_film():
    print("\n--- Tambah Film ---")
    while True:
        film = input("Masukkan nama film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
        if not film:
            break
        if film in daftar_film:
            print(f"Film '{film}' sudah ada dalam daftar. Silahkan masukkan film lain.")
        else:
            daftar_film.append(film)
            simpan_film()
            print(f"Film '{film}' berhasil ditambahkan.")

def hapus_film():
    print("\n--- Hapus Film ---")
    tampilkan_film()
    if daftar_film:
        pilihan = input("Pilih nomor film yang ingin dihapus (atau tekan Enter untuk kembali): ")
        
        if not pilihan:
            return
            
        if pilihan and pilihan.isdigit():
            index = int(pilihan) - 1
            if 0 <= index < len(daftar_film):
                film = daftar_film.pop(index)
                simpan_film()
                print(f"Film '{film}' berhasil dihapus.")
            else:
                print("Nomor film tidak valid.")
    else:
        print("Tidak ada film yang tersedia untuk dihapus.")

def tampilkan_film():
    print("\nDaftar Film:")
    if not daftar_film:
        print("Tidak ada film yang tersedia.")
    else:
        for idx, film in enumerate(daftar_film, 1):
            print(f"{idx}. {film}")

def daftar_tiket():
    print("\n--- Daftar Tiket ---")
    tiket_files = [tiket for tiket in os.listdir(FOLDER_TIKET) if tiket.endswith('.txt')]
    if not tiket_files:
        print("Tidak ada tiket yang telah dibeli.")
    else:
        for tiket_file in tiket_files:
            with open(os.path.join(FOLDER_TIKET, tiket_file), 'r') as file:
                print(file.read())
                print()

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah film")
        print("2. Hapus film")
        print("3. Daftar Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == "1":
            tambah_film()
        elif pilihan == "2":
            hapus_film()
        elif pilihan == "3":
            daftar_tiket()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def beli_tiket():
    tampilkan_film()
    
    pilihan = input("\nPilih nomor film yang ingin ditonton (atau enter untuk kembali): ")
    if not pilihan:
        return
    
    try:
        index = int(pilihan) - 1
        if 0 <= index < len(daftar_film):
            film_terpilih = daftar_film[index]
            id_tiket = f"TICK{random.randint(1000000, 9999999)}"
            tanggal = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file_tiket = os.path.join(FOLDER_TIKET, f"{id_tiket}.txt")
            batas_nama_film = film_terpilih if len(film_terpilih) <= 21 else film_terpilih[:18] + '...'
            
            with open(file_tiket, 'w') as file:
                file.write("+---------------------------------+\n")
                file.write("|           TIKET BIOSKOP         |\n")
                file.write("+---------------------------------+\n")
                file.write(f"| ID Tiket : {id_tiket.ljust(21)}|\n")
                file.write(f"| Film     : {batas_nama_film.ljust(21)}|\n")
                file.write(f"| Tanggal  : {tanggal.ljust(21)}|\n")
                file.write("+---------------------------------+\n")
                file.write("|    Terima kasih telah membeli   |\n")
                file.write("|          tiket Anda!            |\n")
                file.write("+---------------------------------+\n")
            
            print(f"\nTiket berhasil dibeli. ID tiket Anda: {id_tiket}")
            print(f"File tiket telah dibuat: {file_tiket}")
        else:
            print("Nomor film tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan nomor film yang benar.")


def menu_pengunjung():
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. Lihat daftar film")
        print("2. Beli tiket")
        print("3. Kembali")
        pilihan = input("Pilih opsi (1/2/3): ")
        
        if pilihan == "1":
            tampilkan_film()
            input("\nTekan Enter untuk kembali")
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def menu_utama():
    while True:
        print("\n--- Sistem Informasi Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        peran = input("Pilih peran (1/2/3): ")
        
        if peran == "1":
            menu_admin()
        elif peran == "2":
            menu_pengunjung()
        elif peran == "3":
            print("Terima kasih telah menggunakan Sistem Informasi Bioskop.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    buat_struktur_folder()
    muat_data()
    menu_utama()