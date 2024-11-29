saham = float(input("Masukkan harga saham kemarin : "))

saham_today = 105
perper = ((saham - saham_today) / saham_today) * 100
hasil = ["jual", "tahan", "beli"]
index = (perper >= 5) - (perper <= -3) + 1

print(f"Perubahan persentase harga saham : {perper:.2f}%")
print(f"rekomendasi investasi : {hasil[index]}")
