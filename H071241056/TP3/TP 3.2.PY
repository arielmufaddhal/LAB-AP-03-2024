import random 
 
angka_rahasia = random.randint(1, 100) 
percobaan = 5 
 
while percobaan > 0: 
    angka_pemain = int(input("Masukkan angka yang Anda tebak (1-100): ")) 
 
    if angka_pemain < angka_rahasia: 
        print("Angka terlalu kecil.") 
    elif angka_pemain > angka_rahasia: 
        print("Angka terlalu besar.") 
    else: 
        print("Selamat Anda berhasil menebak angka rahasia.") 
        break 
 
    percobaan -= 1 
 
    if percobaan == 0: 
        print(f"Maaf, Anda gagal menebak angka rahasia. Angka rahasia adalah {angka_rahasia}.")