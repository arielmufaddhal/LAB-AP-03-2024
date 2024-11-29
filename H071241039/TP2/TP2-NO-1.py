a = (input("Masukan Panjang sisi a : "))
b = (input("Masukan Panjang sisi b : "))
c = (input("Masukan Panjang sisi c : "))


if (a.isnumeric() and b.isnumeric() and c.isnumeric()) :
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("segitiga sama sisi")
        elif a == b or a == c or b == c:
            print("segitiga sama kaki")
        else:
            print("segitiga sembarang")
    else:
        print ("tidak dapat membentuk segitiga yang valid")
else :
    print("input tidak valid")



a = (input("Masukan Panjang sisi a : "))
b = (input("Masukan Panjang sisi b : "))
c = (input("Masukan Panjang sisi c : "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("segitiga sama sisi")
    elif a == b or a == c or b == c:
        print("segitiga sama kaki")
    else:
        print("segitiga sembarang")
else:
    print ("tidak dapat membentuk segitiga yang valid")