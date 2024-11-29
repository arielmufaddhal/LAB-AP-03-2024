#2
usia = int(input('Masukkan Usia = '))
anggota = input("Apakah Anda Anggota (ya/tidak) = ")

if usia < 5 :
    status = 0
elif 5 <= usia <=12 :
    status = 50.000
elif 13 <= usia <= 59 :
    status = 100.000
else :
    status = 70.000

status_diskon = status-(status*20/100) if anggota=="ya" else status

print(f"harga tiket : Rp.{status_diskon:.3f}")
