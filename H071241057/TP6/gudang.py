
gudang = []

def tambah():
    kode = str(input("Masukkan kode barang: "))
    nama = input("Masukkan nama barang: ")

    while True:
        try :
            jumlah = int(input("Masukkan jumlah barang: "))
            break
        except ValueError :
            print("masukkan angka saja.")

    while True :
        try :
            harga = float(input("Masukkan harga barang: "))
            break
        except ValueError :
            print("masukkan angka saja.")
    
    barang = {
        'kode': kode,
        'nama': nama,
        'jumlah': jumlah,
        'harga': harga
    }
    
    gudang.append(barang)
    print(f"Barang '{nama}' telah ditambahkan ke gudang.")

def hapus():
    while True:
        try :
            index = str(input("Masukkan kode barang yang ingin dihapus: "))
            break
        except ValueError :
            print("masukkan angka bulat yang lebih dari 0.")
            return
        
    for barang in gudang :
        if barang['kode'] == index :
            gudang.remove(barang)
            print(f"Barang telah dihapus dari inventory.")
            return
    print(f"kode barang {index} tidak ditemukan")

def tampilkan():
    if not gudang:
        print("gudang masih kosong.")
        return
    
    print("\nDaftar Barang di gudang:")
    for barang in gudang:
        print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")

def cari():
    while True:
        try :
            index = (input("Masukkan kode barang yang ingin dicari: ")) 
            break
        except ValueError :
            print("masukkan angka bulat yang lebih dari 0.")
            return
    for barang in gudang :
        if barang['kode'] == index :
            print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
            return
    print(f"kode barang {index} tidak ditemukan")
        
    
def perbarui():
    index = input("Masukkan kode barang yang ingin diperbarui: ")
    for barang in gudang:
        if barang['kode'] == index:
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            harga_baru = float(input("Masukkan harga baru: "))
            barang['jumlah'] = jumlah_baru
            barang['harga'] = harga_baru
            print(f"Data barang '{barang ['nama']}' telah diperbarui.")
            return
    print(f"Kode barang '{index}' tidak ditemukan dalam gudang.")


    
while True:
    print("\n===== MENU INVENTORY BARANG =====")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")
    print("===================================")
    choice = input("Pilih opsi (1-6): ")
        
    if choice == '1':
        tambah()
    elif choice == '2':
        hapus()
    elif choice == '3':
        tampilkan()
    elif choice == '4':
        cari()
    elif choice == '5':
        perbarui()
    elif choice == '6':
        print("Terima kasih telah menggunakan program gudang barang.")
        break
    else:
        print("Opsi tidak valid. Silakan coba lagi.")
    
            



