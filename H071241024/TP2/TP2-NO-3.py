NilaiAkhir = int(input("Masukkan Nilai Akhir: "))
PersentaseKehadiran = int(input("Masukkan Persentase Kehadiran: "))

if PersentaseKehadiran >= 75:
    if 100 >= NilaiAkhir >= 85:
        print ("Lulus dengan predikat A")
    elif 84 >= NilaiAkhir >= 70:
        print ("Lulus dengan predikat B")
    elif 69 >= NilaiAkhir >= 60:
        print ("Lulus dengan predikat C")
    elif NilaiAkhir < 60:
        print ("Lulus dengan predikat C")
    else:
        print ("Nilai tidak valid")

elif PersentaseKehadiran < 75:
    if 100 >= NilaiAkhir >= 85:
        print ("Lulus dengan predikat A")
    elif 84 >= NilaiAkhir >= 70:
        print ("Lulus dengan predikat B")
    elif 69 >= NilaiAkhir >= 60:
        print ("Lulus dengan predikat C")
    elif NilaiAkhir < 60:
        print ("Tidak Lulus")
    else:
        print ("Nilai tidak valid")
