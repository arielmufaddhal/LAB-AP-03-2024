'''
1. Fungsi Utama:
- Menambah Barang
- Menghapus Barang
- Menampilkan Daftar Barang 
- Mencari Barang
- Mengupdate Data Barang
'''

inventory = {}

def menu():
    print("=== Menu Inventory Barang")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def menambah_barang():
    print("===Tambahkan Barang===")
    id = input("Masukkan id Barang = ")
    
    if id in inventory:
        print("id barang sudah ada")
    else:
        nama = input("Masukkan nama Barang = ")
        jumlah = input("Masukkan jumlah Barang = ")
        harga = input("Masukkan harga Barang = ")

        inventory[id] = {"nama": nama, "jumlah": jumlah, "harga": harga}
        print("Barang berhasil di tambahkan")

def hapus_barang():
    print("===Menghapus Barang===")
    id = input("Masukkan id yang ingin anda hapus = ")

    if id in inventory :
        del inventory[id]
        print("Barang telah berhasil dihapus")
    else:
        print("Id barang tidak tidak ditemukan")

def tampilkan_daftar_barang():
    if inventory:
        print("===Daftar Barang===")
        print(inventory)
        for id, data in inventory.items():
            print(f"id: {id}, nama: {data["nama"]}, jumlah: {data["jumlah"]}, harga: {data["harga"]}")
    else:
        print("Barang tidak ditemukan di inventory")

def cari_barang():
    print("====Cari Barang===")
    id = input("Masukkan id yang ingin dicari =")
    if id in inventory:
        data = inventory[id]
        print("id :",id ,", nama barang =", data["nama"],", jumlah barang =", data["jumlah"],", harga barang =", data["harga"])
    else:
        print("id tidak ditemukan")

def update_barang():
    print("===Update Barang===")
    id = input("Masukan id barang yang ingin di update =")

    if id in inventory:
        nama_baru = input("Masukkan nama barang baru (kosongkan jika tidak ingin mengubah nama) =")
        jumlah_baru = input("Masukkan jumlah barang baru (kosongkan jika tidak ingin mengubah jumlah) =")
        harga_baru = input("Masukkan harga barang baru (kosongkan jika tidak ingin mengubah harga) =")

        if nama_baru != "":
            inventory[id]["nama"] = nama_baru
        if jumlah_baru != "":
            inventory[id]["jumlah"] = jumlah_baru
        if harga_baru != "":
            inventory[id]["harga"] = harga_baru
        
        print("Data barang berhasil diupdate!")
    
    else:
        print("id barang tidak ditemukan!")


def main():
    while True:
        menu()
        opsi = int(input("pilih opsi 1-6 = "))
    
        if opsi == 1 :
            menambah_barang()
        elif opsi == 2 :
            hapus_barang()
        elif opsi == 3 :
            tampilkan_daftar_barang()
        elif opsi == 4 :
            cari_barang()
        elif opsi == 5 :
            update_barang()
        elif opsi == 6 :
            print("program selesai, bye")
            break
        else:
            print("pilih opsi yang ada saja!")
    
main()

