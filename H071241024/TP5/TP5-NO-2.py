def acronym(kalimat):
    return ''.join(kata[0].upper() for kata in kalimat.split())

kalimat = input("Masukkan kalimat: ")
hasil = acronym(kalimat)
print(hasil)