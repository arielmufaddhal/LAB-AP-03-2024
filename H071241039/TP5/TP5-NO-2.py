def akronim(kalimat):
    split = kalimat.split(" ")
    akronim = ""
    print(split)
    for i in split :
        akronim += i[0].upper()
    print(akronim)
    
kalimat = input("masukkan kalimat yang ingin di singkat = ")
akronim(kalimat)