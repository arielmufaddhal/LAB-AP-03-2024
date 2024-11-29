harga = int(input("masukkan harga :"))
uang = int(input("masukkan uang :"))
kembali = uang - harga
pecahan = [100000,50000,20000,10000,5000,1000,500,200,100]
print(f"kembaliannya adalah {kembali}")

if uang < harga :
    print("maaf, uang tidak cukup")
elif uang==harga :
    print("uang pas")
else :
    for i in pecahan :
        lembar = kembali//i
        if lembar > 0 :
            print(f"{lembar} lembar uang {i}")
        kembali %= i 
