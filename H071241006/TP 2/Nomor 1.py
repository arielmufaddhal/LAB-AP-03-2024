a = input("Masukkan panjang sisi pertama:")
b = input("Masukkan panjang sisi kedua:")
c = input("Masukkan panjang sisi ketiga:")

if a + b >= c or b + c <= a or a + c <= b:
    
    if a == b == c:
        print("Segitiga sama sisi")
    elif a == b or b == c or c == a:
        print("Segitiga sama kaki")
    else :
        print("Segitiga sembarang")

else :
    print("Tidak dapat membentuk segitiga yang valid")