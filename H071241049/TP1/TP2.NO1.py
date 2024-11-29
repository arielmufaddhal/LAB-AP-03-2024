print("## Program Saham ##")
print()

saham = float(input(" Harga Saham Kemarin : "))
saham_hari_ini = 105.0
angka = float (saham_hari_ini)
print (angka)

persentase = (saham_hari_ini - saham)/saham * 100
print (persentase)

rekomendasi_dict = {
    persentase >5: "Beli",
    (-3 <= persentase <5): "Tahan",
    persentase <= -3: "Jual"
}

print(f"Persentase = {persentase:.2f}%")
print(rekomendasi_dict[True])