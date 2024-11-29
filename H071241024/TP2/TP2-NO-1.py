sisi_1 = int(input("Masukkan sisi 1: "))
sisi_2 = int(input("Masukkan sisi 2: "))
sisi_3 = int(input("Masukkan sisi 3: "))

if sisi_1 == sisi_2 == sisi_3:
    print ("Segitiga Sama Sisi")
elif sisi_1 != sisi_2 == sisi_3:
    print ("Segitiga Sama Kaki")
elif sisi_1 == sisi_2 != sisi_3:
    print ("Segitiga Sama Kaki")
elif sisi_1 == sisi_3 != sisi_2:
    print ("Segitiga Sama Kaki")
else:
    print ("Tidak dapat membentuk segitiga yang valid")