usia = int(input("masukan usia: "))
anggota = str(input("apakah anda anggota (y/t): "))
tiket = int(input("harga tiket: "))

if usia < 5 and usia >= 0 :
    print("harga tiket gratis")

elif 5 <= usia <= 12:
   
    if anggota == "y" :
          print("harga tiket 40.000")
    else :
        print("harga tiket 50.000")
       
elif 13 <= usia <= 59:

    if anggota == "y" :
        print("harga tiket 80.000")
    else :
        print("harga tiket 100.000")
elif usia >= 60:
    print("harga tiket 60.000")
else:
    print("umur tidak valid")