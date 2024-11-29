harga_saham_kemarin = float(input("masukkan harga saham kemarin:"))
harga_saham_hari_ini = 105

perubahan_persentase_harga_saham = ((harga_saham_hari_ini - harga_saham_kemarin) / harga_saham_kemarin) * 100
if perubahan_persentase_harga_saham > 5:
  rekomendasi = "Beli"
elif 5>= perubahan_persentase_harga_saham > -3:
  rekomendasi = "Tahan"
else:
  rekomendasi = "Jual"

print(f"perubahan persentase harga saham: {perubahan_persentase_harga_saham:.2f}%")
print(f"rekomendasi investasi:{rekomendasi}")