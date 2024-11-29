PecahanUang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

TotalHarga = int(input("Masukkah total harga: "))
UangDiberikan = int(input("Masukkah uang yang diberikan: "))

if TotalHarga > UangDiberikan:
    print("uang tidak cukup")
else:
    Kembalian = UangDiberikan - TotalHarga
    print (f'Kembalian : {Kembalian:,}')

    for Pecahan in PecahanUang:
        JumlahLembar = Kembalian // Pecahan
        Kembalian = Kembalian % Pecahan
        if JumlahLembar > 0:
            print(f'{JumlahLembar} lembar Rp {Pecahan:,}')
            
        