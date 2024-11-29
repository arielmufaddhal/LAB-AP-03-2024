# Tiket wahana
usia = int (input("Masukkan usia: "))

if usia <5:
    harga = 0
elif 5 < usia < 12:
    harga = 50000
elif 13 < usia < 59:
    harga = 100000
else:
    harga = 70000

keanggotaan = input("Apakah anda anggota?(Ya/Tidak)")
diskon = harga - (harga * 20/100)
harga_tiket = diskon if keanggotaan == "Ya" else harga
print (f'Harga Tiket: Rp{int(harga_tiket)}')