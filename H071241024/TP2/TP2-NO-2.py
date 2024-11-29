usia = int(input("Masukkan Usia: "))
keanggotaan = (input("Apakah Anda Anggota (ya/tidak): ")).lower()

if usia < 5:
    HargaTiket = 0
elif 5 <= usia <= 12:
    HargaTiket = 50000
elif 13 <= usia <= 59:
    HargaTiket = 100000
else:
    HargaTiket = 70000
    
HargaDiskon = int(HargaTiket * 0.8 if keanggotaan == "ya" else HargaTiket)

if HargaTiket == 0:
    print("Harga Tiket : Gratis")
else:
    print (f'Harga Tiket : Rp.{HargaDiskon}')