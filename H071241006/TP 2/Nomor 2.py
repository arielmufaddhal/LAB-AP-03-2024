kategori_usia = int(input("Masukkan usia:"))
diskon_keanggotaan = (input("Apakah anda anggota (ya/tidak):"))

harga = 0

if kategori_usia < 5 :
    harga = "gratis"
elif kategori_usia > 5 and kategori_usia < 12 :
    harga = 50000
elif kategori_usia > 13 and kategori_usia < 59 :
    harga = 100000
elif kategori_usia > 60 :
    harga = 70000

if diskon_keanggotaan == "ya" :
    harga = harga * 0.8

print("harga tiket:", harga)