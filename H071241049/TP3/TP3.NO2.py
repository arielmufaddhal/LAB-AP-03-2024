#Permainan
import random
angka_rahasia = random.randint (1, 100)
percobaan = 0
max_percobaan = 5

print("Selamat datang di permainan Tebak Angka!")
print("Saya sudah memilih angka antara 1 hingga 100.")
print("Anda memiliki 5 kali percobaan untuk menebak angka tersebut.")
print("Ketik '0' untuk menghentikan permainan kapan saja.")

while percobaan < max_percobaan:
    tebakan = input("Masukkan tebakan Anda: ")
    if tebakan == '0':
        print("Permainan telah berhenti")
        break

#Konversi keangka
    try:
        tebakan = int(tebakan)
    except:
        print("Input harus berupa angka")
        continue

    percobaan += 1
    if tebakan == angka_rahasia:
        print("Selamat! Anda berhasil menebak angka yang tepat")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")

    if percobaan == max_percobaan:
        print(f"Anda telah mencapai maksimal percobaan. Angka rahasianya adalah {angka_rahasia}.")
