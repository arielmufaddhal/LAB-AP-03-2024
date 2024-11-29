import os
from datetime import datetime as dt

def main():
    while True:
        print("\n --- Sistem Pemesanan Tiket Bioskop --- ")
        print("1. Admin ")
        print("2. Pengunjung ")
        print("3. Keluar ")
        while True:
            try:
                peran = int(input("\nPilih peran (1/2/3): "))
                break
            except ValueError:
                print("input salah")

        if peran == 1 :
            if not os.path.exists("/tugas lab 7/film") :
                os.mkdir("film")
            if not os.path.exists("/tugas lab 7/tickets") :
                os.mkdir("tickets")
            admin()

        elif peran == 2 :
            if not os.path.exists("/tugas lab 7/film") :
                os.mkdir("film")
            if not os.path.exists("/tugas lab 7/tickets") :
                os.mkdir("tickets")
            pengunjung()

        elif peran == 3 :
            print("terimakasih telah menggunakan program ini.")
            return
        
        else :
            print("masukkan hanya (1/2/3)")

def admin():
    while True:
        print("\n --- Menu Admin --- ")
        print("1. Tambah film ")
        print("2. Hapus film ")
        print("3. Daftar tiket ")
        print("4. Kembali ")
        while True:
            try:
                opsi = int(input("\nPilih opsi (1/2/3/4): "))
                break
            except ValueError :
                print("salah")        
        if opsi == 1 :
            tambahfilm()

        elif opsi == 2 :
            hapusfilm()

        elif opsi == 3 :
            print("\n --- Daftar Tiket --- ")
            daftartiket()

        elif opsi == 4 :    
            return
        
        else :
            print("input hanya (1/2/3/4)")
                    
def tambahfilm() :
    os.chdir("/tugas lab 7/film")

    while True :
        print("\n --- Tambah Film ---")
        film = input("Masukkan judul film yang ingin ditambahkan (tekan enter untuk kembali) : ")
        file_path = f"/tugas lab 7/film/{film}"

        if not film :
            print("Kembali ke menu admin.")
            os.chdir("/tugas lab 7")
            break

        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"Film: {film}\n")
            print(f"Film '{film}' berhasil ditambahkan.")

        elif os.path.exists(file_path):
            print(f"Film '{film}' sudah ada.")



def hapusfilm() :

    while True:
        daftar = os.listdir("film")

        print("\n --- Hapus Film --- ")
        print("Daftar film :")
        daftarfilm()

        if not daftar :
            print ("kembali ke menu admin.")
            return
        
        print("0.Kembali")

        try:
            pilihan = int(input("Masukkan nomor film yang ingin dihapus (ketik 0 untuk kembali): "))
            if  pilihan== 0:
                break
            index = int(pilihan) - 1
            os.remove(f"film/{daftar[index]}")
            print(f"Film {daftar[index]} berhasil dihapus.")

        except (ValueError):
            print("Masukkan angka yang valid.")

        except OSError as e:
            print(f"Error: {e}")

def daftartiket() :
    if os.path.exists("tickets"):
        listtiket = os.listdir("tickets")

    else:
        print('\nDirektori tickets tidak ditemukan.\n')
        return

    if not listtiket:
        print('\nTidak ada tiket.')
        return
    
    else :
        urut = 1
        for i in (listtiket) :
            print(f"{urut}. {i}")
            urut+=1

def daftarfilm() :
    if os.path.exists("film"):
        listfilm = os.listdir("film")

    else:
        print('\nDirektori film tidak ditemukan.\n')
        return

    if not listfilm:
        print('Tidak ada film.')
        return
    
    else :
        urut = 1
        for i in (listfilm) :
            print(f"{urut}. {i}")
            urut+=1


def pengunjung() :
    while True:
        print("\n --- Menu Pengunjung --- ")
        print("1. Daftar film ")
        print("2. Beli tiket ")
        print("3. Kembali ")
        opsi = int(input("\nPilih opsi (1/2/3): "))
        
        if opsi == 1 :
            print("\n --- Daftar Film --- ")
            daftarfilm()

        elif opsi == 2 :
            belitiket()

        elif opsi == 3 :
            return
        
        else :
            print("input hanya (1/2/3)")

def belitiket():
    daftar = os.listdir("film")

    while True :
        print("\n --- Beli Tiket --- ")
        print("Daftar film :")
        daftarfilm()

        if not daftar :
            return
        
        print("0. kembali")

        os.chdir("/tugas lab 7/tickets")

        index = int(input("Masukkan nomor film yang ingin dibeli (masukkan 0 untuk kembali) : "))
        if index == 0:
            os.chdir("/tugas lab 7")
            break
        now = dt.now()
        format = now.strftime("%d%m%Y%H%M%S")
        id = f"TICK{format}"
        film = daftar[index-1]
        if index > len(daftar) or index < 1:
            print("Nomor film tidak valid. Coba lagi.")
            continue
        path = f"/tugas lab 7/tickets/{id}"
        path_tiket = f"/tickets/{id}"
        with open(path, "w") as f:
            f.write(f"""
                    +-----------------------------------------------+
                    |           TIKET BIOSKOP                       |
                    +-----------------------------------------------+
                    | ID Tiket : {id}                 |
                    | Film     : {film}|
                    | Tanggal  : {now}               |
                    +-----------------------------------------------+
                    |   Terima kasih telah membeli                  |
                    |          tiket Anda!                          |
                    +-----------------------------------------------+""")
            print(f"tiket berhasil dibeli. ID tiket anda : {id}")
            print(f"file tiket telah dibuat: {path_tiket}")
        os.chdir("/tugas lab 7")
    
main()
