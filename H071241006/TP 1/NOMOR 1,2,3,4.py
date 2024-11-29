#Tugas Praktikum 1
#soal 1
# harga_kemarin = int(input("masukkan harga saham kemarin:"))
# harga_hari_ini = 105.0
#
# persentase_perubahan = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100
#
# hasil = "beli" * (persentase_perubahan > 5) + \
#     "tahan" * (persentase_perubahan < 5) * (persentase_perubahan > -3) + \
#     "jual" * (persentase_perubahan < -3)
#
# print (hasil)
# print (f"{persentase_perubahan: .2f}")
#
# #soal 2
# karakter = input("Masukkan karakter: ")
# kalimat = input("Masukkan kalimat: ")
#
# hasil = ((karakter in kalimat) * "Karakter merupakan bagian dari Kalimat" +
#     (karakter not in kalimat) * "Karakter tidak ditemukan dalam Kalimat")
#
# print(hasil)

#soal 3
jumlah_detik = int(input("Masukkan jumlah detik: "))

jam = jumlah_detik // 3600
menit = (jumlah_detik % 3600)//60
detik =jumlah_detik % 60

waktu_format = f"{jam}:{menit}:{detik}"


print(waktu_format)

# #soal 4
# celcius = int(input("masukkan celcius: "))
# fahrenheit = (celcius * 9/5) + 32
# reamur = celcius * 4/5
# kelvin = celcius + 273
#
# print(f"Suhu dalam Kelvin: {kelvin:.2f} K")
# print(f"Suhu dalam Reamur: {reamur:.2f} °Re")
# print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")
#
# print(hash)
