import random

AngkaAcak = random.randint(1, 100)
percobaan = 0
MaksPercobaan = 5

while percobaan < MaksPercobaan:
    try:
        tebakan = int(input(f"Percobaan {percobaan+1}: Masukkan tebakan Anda (0 untuk berhenti): "))
    except ValueError:
        print("Masukkan angka yang valid.")
        continue

    if tebakan == 0:
        print("Permainan Dihentikan")
        break
    
    percobaan += 1
    
    if tebakan == AngkaAcak:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan < AngkaAcak:
        print("Angka terlalu kecil.")
    else:
        print("Angka terlalu besar.")

    if percobaan == MaksPercobaan:
        print("Percobaan Habis")
        print(f"Angka yang benar adalah {AngkaAcak}")