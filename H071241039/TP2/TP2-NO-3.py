nilai_akhir = int(input("masukan nilai akhir : "))
kehadiran = int(input("masukan persentase kehadiran : "))
if (kehadiran >= 0 or kehadiran >= 100 ) and ( nilai_akhir >= 0 or nilai_akhir >= 100):
    print("input tidak valid")
else:
    if kehadiran < 75  :
        print("Tidak Lulus (kehadiran kurang dari 75%)")
    elif nilai_akhir >= 85:
        print("lulus dengan predikat A")
    elif nilai_akhir >= 70:
        print("lulus dengan predikat B")
    elif nilai_akhir >= 60:
        print("lulus dengan predikat C")
    elif nilai_akhir < 60:
        nilai_tugas_tambahan = int(input("masukan nilai rata-rata tugas tambahan : "))
        if nilai_tugas_tambahan >= 70 and kehadiran >= 75:
            print("lulus dengan predikat C")
        else:
             print("anda tidak lulus")