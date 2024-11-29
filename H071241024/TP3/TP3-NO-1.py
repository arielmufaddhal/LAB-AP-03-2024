baris = "0"
try:
    baris = int(input("Masukkan Jumlah Baris : "))
except:
    baris = int(baris)
finally:
    if baris > 0:    
        if baris % 2 == 0:    
            for i in range (1, (baris // 2) + 1):
                print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
            for i in range ((baris // 2), 0, -1):
                print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
        elif baris % 2 != 0:
            for i in range (1, (baris // 2) + 2):
                print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
            for i in range ((baris // 2), 0, -1):
                print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
    else:
        print("Masukkan angka yang valid")