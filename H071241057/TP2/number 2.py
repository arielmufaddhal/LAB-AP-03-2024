usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota? (y/n): ")

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

uji = False
final = 0

if (anggota.lower())== "y" :
    final = harga * 0.8 
elif (anggota.lower()) == "n" :
    final = harga

list = ["input tida valid", f"Harga tiket yang harus dibayar: Rp{final}"]
print(list[((anggota.lower()) == "y") or ((anggota.lower()) == "n")])
