def is_chipher(text, pergeseran):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    angka = "0123456789"

    perubahan_text = ""

    for karakter in text :
        if karakter in huruf_kecil :
            indeks = huruf_kecil.index(karakter)
            indeks_baru = (indeks + pergeseran) % 26
            perubahan_text += huruf_kecil[indeks_baru]
        elif karakter in huruf_besar:
            indeks = huruf_besar.index(karakter)
            indeks_baru = (indeks + pergeseran) % 26  
            perubahan_text += huruf_besar[indeks_baru]
        elif karakter in angka :
            indeks = angka.index(karakter)
            indeks_baru = (indeks+pergeseran) %10
            perubahan_text += angka[indeks_baru]
        else: 
            perubahan_text += karakter

    print(f"Teks: {text}")
    print(f"Pergeseran: {pergeseran}")
    print(f"hasil perubahan: {perubahan_text}")

try :
    text = input("masukkan string = ")
    pergeseran = int(input("masukkan jumlah pergeseran = "))
    is_chipher(text, pergeseran)

except:
    print("masukkan angka untuk pergeseran")


