final = float(input("Masukkan nilai akhir mahasiswa: "))
kehadiran = float(input("Masukkan persentase kehadiran mahasiswa: "))

if kehadiran < 75:
    print("Tidak Lulus karena kehadiran kurang dari 75%.")
elif final >= 85:
    print("Lulus dengan Predikat A.")
elif final >= 70:
    print("Lulus dengan Predikat B.")
elif final >= 60:
    print("Lulus dengan Predikat C.")
elif final < 60:

   tambahan = float(input("masukkan nilai tambahan :"))
   if tambahan >= 70 :
       print("Lulus dengan Predikat C.")
   else :
       print("Tidak lulus.")
