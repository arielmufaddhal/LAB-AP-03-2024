pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# total dari harga yg dbyar 
total_harga = int(input("Masukkan total harga: "))
uang_dibayar = int(input("Masukkan uang yang diberikan: "))

if uang_dibayar > total_harga:
    #  kembalian
    kembalian = uang_dibayar - total_harga
    print("Kembalian:")
    for pecahan_uang in pecahan:
        jumlah_pecahan = kembalian // pecahan_uang
        kembalian %= pecahan_uang
    if jumlah_pecahan > 0:
        print(f"{jumlah_pecahan} lembar Rp {pecahan_uang}")
else:
    print("uang anda kurang")

# jumlah pecahan uang
