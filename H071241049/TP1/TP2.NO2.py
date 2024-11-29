print("## Program Karakter dalam Kalimat ##")
print()

karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

cek_karakter = karakter not in kalimat
hasil = ["ada", "tdk ada"][cek_karakter]

print (hasil)