#Kasir
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

total_harga = int(input("Masukkah total harga: "))
uang_diberikan = int(input("Masukkah uang yang diberikan: "))

if total_harga > uang_diberikan:
    print("uang tidak cukup")
else:
    kembalian = uang_diberikan - total_harga
    print (f'kembalian : {kembalian:,}')

    for pecahan in pecahan_uang:
        jumlah_lembar = kembalian // pecahan
        kembalian = kembalian % pecahan
        if jumlah_lembar > 0:
            print(f'{jumlah_lembar} lembar Rp {pecahan:,}')
