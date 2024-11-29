usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota (ya/tidak): ").lower()

# Menghitung harga tiket berdasarkan usia
if usia <= 5:
    harga_tiket = 0  # Tiket gratis untuk usia 5 tahun ke bawah
elif 6 <= usia <= 12:
    harga_tiket = 50000
elif 13 <= usia <= 59:
    harga_tiket = 100000
else:
    harga_tiket = 70000  # Diskon untuk lansia

# Menghitung diskon keanggotaan dengan ternary operator
if anggota == "ya":
   harga_tiket *= 0.8
else:
    harga_tiket = harga_tiket

# Menampilkan harga tiket
print(f"Harga tiket: Rp.{harga_tiket:.0f}")