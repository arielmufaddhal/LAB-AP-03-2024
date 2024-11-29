import random

angka_rahasia = random.randint(1, 100)
percobaan = 5
while percobaan > 0:
    try : 
        tebakan = int(input("masukan tebakan anda (0 untuk berhenti): "))
    except :
        print("masukin angka bukan kalimat. ULANG!!!")
        continue
    if tebakan == angka_rahasia:
        print("selamat! anda menebak angka dengan benar.")
        break
    elif tebakan == 0 :
        print("anda sudah keluar! game telah berakhir")
        break
    elif tebakan > angka_rahasia:
        percobaan -= 1
        print("angka terlalu besar.")
        print(f"tersisa {percobaan} kesempatan lagi")
    elif tebakan < angka_rahasia:
        percobaan -= 1
        print("angka terlalu kecil.")
        print(f"tersisa {percobaan} kesempatan lagi")
else:
    print(f"Percobaan anda sudah habis. Angka yang benar adalah {angka_rahasia}.")