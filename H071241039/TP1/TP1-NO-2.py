karakter = input("masukan karakter: ")
kalimat = input("masukan kalimat: ")

output = karakter in kalimat
print (output)

pesan = ["tidak ditemukan dalam", "merupakan bagian dari"][output]

hasil = f"{karakter} {pesan} '{kalimat}'"
print(hasil)