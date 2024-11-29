# 3
nilai = int(input('Masukkan nilai akhir          = '))
kehadiran = int(input('Masukkan persentase kehadiran = '))

if kehadiran >= 75 :
    if 85 <= nilai <=100 :
        Nilai = "A"
    elif 70 <= nilai <= 84 :
        Nilai = "B"
    elif nilai <= 69:
        Nilai = "C"
    print(f'Lulus dengan predikat {Nilai}')
else :
    print("Tidak Lulus")
