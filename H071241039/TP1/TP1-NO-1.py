harga_kemarin = int(input("masukan harga saham kemarin :"))
harga_hari_ini = 105.0

persentase_perubahan = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100
print (persentase_perubahan)

hasil = "beli" * (persentase_perubahan > 5) + \
    "tahan" * (persentase_perubahan < 5) * (persentase_perubahan > -3) + \
    "jual" * (persentase_perubahan < -3)

print (hasil)
print (f"{persentase_perubahan:.2f}")