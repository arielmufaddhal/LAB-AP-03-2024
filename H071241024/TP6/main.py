inventory = {}

def tambah_barang():
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    
    while True:
        try:
            jumlah = int(input("Masukkan jumlah barang: "))
            if jumlah <= 0:
                raise ValueError("Jumlah harus bilangan bulat positif.")
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Mohon masukkan bilangan bulat positif.")
    
    while True:
        try:
            harga = float(input("Masukkan harga per unit: "))
            if harga <= 0:
                raise ValueError("Harga harus bilangan positif.")
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Mohon masukkan bilangan positif.")
    
    inventory[kode] = {"nama": nama, "jumlah": jumlah, "harga": harga}
    print("Barang berhasil ditambahkan.")

def hapus_barang():
    kode = input("Masukkan kode barang yang akan dihapus: ")
    if kode in inventory:
        del inventory[kode]
        print(f"Barang dengan kode {kode} berhasil dihapus dari inventory.")
    else:
        print(f"Barang dengan kode {kode} tidak ditemukan dalam inventory.")

def tampilkan_barang():
    if inventory:
        print("Daftar Barang:")
        for kode, barang in inventory.items():
            print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
    else:
        print("Inventory kosong.")

def cari_barang():
    print("Cari berdasarkan (1) Kode atau (2) Nama: ")
    pilihan = input()
    if pilihan == "1":
        kode = input("Masukkan kode barang: ")
        if kode in inventory:
            barang = inventory[kode]
            print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: {barang['harga']}")
        else:
            print(f"Barang dengan kode {kode} tidak ditemukan dalam inventory.")
    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        found = False
        for kode, barang in inventory.items():
            if barang['nama'].lower() == nama.lower():
                print(f"Kode: {kode}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga per unit: {barang['harga']}")
                found = True
        if not found:
            print(f"Barang dengan nama {nama} tidak ditemukan dalam inventory.")
    else:
        print("Pilihan tidak valid.")

def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    if kode in inventory:
        while True:
            try:
                jumlah_baru = int(input("Masukkan jumlah baru: "))
                if jumlah_baru <= 0:
                    raise ValueError("Jumlah harus bilangan bulat positif.")
                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Mohon masukkan bilangan bulat positif.")
        
        while True:
            try:
                harga_baru = float(input("Masukkan harga per unit baru: "))
                if harga_baru <= 0:
                    raise ValueError("Harga harus bilangan positif.")
                break
            except ValueError as e:
                print(f"Error: {e}")
                print("Mohon masukkan bilangan positif.")
        
        inventory[kode]['jumlah'] = jumlah_baru
        inventory[kode]['harga'] = harga_baru
        print("Data barang berhasil diperbarui.")
    else:
        print(f"Barang dengan kode {kode} tidak ditemukan dalam inventory.")

def menu():
    while True:
        print("\n=== Menu Inventori Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program inventory.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()