nilai_akhir = int(input("Masukkan nilai akhir: "))
persentase_kehadiran = int(input("Masukkan persentase kehadiran (%): "))


# Memeriksa apakah mahasiswa memenuhi syarat kehadiran
if persentase_kehadiran <100 and nilai_akhir < 100 and persentase_kehadiran >= 0 and nilai_akhir >=0 :
    if persentase_kehadiran < 75:
        print("Tidak Lulus: Kehadiran kurang dari 75%.")
    else:
    # Memeriksa kelulusan berdasarkan nilai akhir dan tugas tambahan
        if nilai_akhir >= 85:
            print("Lulus dengan Predikat A.")
        elif 70 <= nilai_akhir < 85:
            print("Lulus dengan Predikat B.")
        elif 60 <= nilai_akhir < 70:
            print("Lulus dengan Predikat C.")
        elif nilai_akhir < 60:
            # Memeriksa apakah mahasiswa memenuhi syarat tugas tambahan untuk lulus dengan C
            tugas_tambahan = int(input("masukkan nilai tugas tambahan:"))
            if tugas_tambahan > 70:
                print("Lulus dengan Predikat C (karena tugas tambahan mencukupi).")
            else:
                print("Tidak Lulus karena nilai akhir di bawah 60 dan tugas tambahan tidak mencukupi.")
else :
    print("jumlah melebihi nilai presentasi")

            