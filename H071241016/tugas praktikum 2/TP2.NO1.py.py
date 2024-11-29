a = (input("Masukkan panjang sisi a: "))
b = (input("Masukkan panjang sisi b: "))
c = (input("Masukkan panjang sisi c: "))


if (a.isnumeric() and b.isnumeric() and c.isnumeric()):
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c and a + c > b and b + c > a:

    # Memeriksa jenis segitiga
        if a == b == c: 
            print("Segitiga Sama Sisi")
        elif a == b or b == c or a == c:
            print("Segitiga Sama Kaki")
        else:
            print("Segitiga Sembarang")
    else:
        print("Tidak dapat membentuk segitiga yang valid") 
else:
    print("INPUT TIDAK VALID")
    

  