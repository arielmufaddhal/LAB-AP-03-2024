karakter = input("Masukkan satu karakter: ")
kalimat = input("Masukkan kalimat: ")

hasil = karakter  not in kalimat
output = ["ditemukan", "tidak ditemukan"]


print(f'{karakter} {output[hasil]} dalam kalimat "{kalimat}"')
