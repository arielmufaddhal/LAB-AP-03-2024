nilai_akhir = float(input("Masukkan nilai akhir:"))
persentase_kehadiran = float(input("Masukkan persentase kehadiran:"))


if persentase_kehadiran < 75 :
    print("Tidak lulus")
if 85 <= nilai_akhir <= 100:
    print("Lulus dengan predikat A")
elif 70 <= nilai_akhir <= 85:
    print("Lulus dengan Predikat B")
elif 60 <= nilai_akhir <= 70:
    print("Lulus dengan Predikat C")
else:
    print("Tidak lulus")
