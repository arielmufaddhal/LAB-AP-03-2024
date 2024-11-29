saham_hari_ini = float(input('masukkan angka saham hari ini ='))
saham_kemarin = 105.0
perhitungan_saham = ((saham_kemarin-saham_hari_ini)/saham_hari_ini)*100

rekomendasi = {
    perhitungan_saham > 5: "Beli" ,
    perhitungan_saham >= -3: "Tahan",
    perhitungan_saham <= 5: "Tahan",
    perhitungan_saham > 5: "jual"
}

hasil = rekomendasi[True]
print(type(rekomendasi))
print(f'perubahan persentase harga saham = {perhitungan_saham:.2f}%')
print(f'rekomendasi investasi = {hasil}')