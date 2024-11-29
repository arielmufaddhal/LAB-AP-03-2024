import random

# Generate angka acak antara 1 sampai 100
angka_rahasia = random.randint(1, 100)

maksimal_percobaan = 5
percobaan = 0

print("HALOO, Selamat datang di permainan Tebak Angka!")
print("Tebak angka antara 1 sampai 100.")

while percobaan < maksimal_percobaan:
    tebakan = input("Masukkan tebakan Anda: ")
    
    # Jika pemain ingin berhenti
    if tebakan.lower() == '0':
        print("Anda memilih untuk SETUPPPPPPPP.")
        break

    # Konversi tebakan menjadi angka
    try:
        tebakan = int(tebakan)
    except ValueError:
        print("Masukkan harus angka.")
        continue

    percobaan += 1

    if tebakan == angka_rahasia:
        print("Selamat! Anda betul ANG ANG ANG.")
        break
    elif tebakan > angka_rahasia:
        print("ANGKA TERLALU GUEDE.")
    else:
        print("ANGKA TERLALU IMOET.")
    
if percobaan == maksimal_percobaan:
    print("Anda kehabisan percobaan. Angka rahasianya adalah:", angka_rahasia)

