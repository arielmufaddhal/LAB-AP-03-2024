def pergeseran_karakter(teks, geser):
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for huruf in teks:
        if huruf in huruf_besar:  
            posisi = (huruf_besar.index(huruf) + geser) % 26
            hasil += huruf_besar[posisi]
        elif huruf in huruf_kecil:
            posisi = (huruf_kecil.index(huruf) + geser) % 26
            hasil += huruf_kecil[posisi]
        elif huruf.isdigit():
            posisi = (int(huruf) + geser)
            hasil += str(posisi)
        else:
            hasil += huruf

    return hasil

while True:
    try:
        teks_awal = input("Masukkan String: ")
        pergeseran = int(input("Masukkan jumlah pergeseran: "))
        break
    except ValueError:
        print("Masukkan Angka yang benar")

hasil_enkripsi = pergeseran_karakter(teks_awal, pergeseran)

print(f"Text : {teks_awal}")
print(f"Shift : {pergeseran}")
print(f"Cipher: {hasil_enkripsi}")