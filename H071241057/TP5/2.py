def acronym (x) :
    
    akronim=""
    for word in x.split("-"):
        akronim += word[0].upper() 

    return akronim

isi = input("masukkan kata atau kalimat :")

print(acronym(isi))
