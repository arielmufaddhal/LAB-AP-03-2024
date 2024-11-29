def enkripsi(text, shift):
    besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kecil = "abcdefghijklmnopqrstuvwxyz"
    angka = "0123456789"
    
    hasil = ""

    for huruf in text:

        if huruf in kecil:
            index = kecil.index(huruf)
            akhir = (index + shift) % 26
            hasil += kecil[akhir]
        
        elif huruf in besar:
            index = besar.index(huruf)
            new_index = (index + shift) % 26
            hasil += besar[new_index]

        elif huruf in angka:
            index = angka.index(huruf)
            if shift % 10 == 0:
                new = shift + 1
                new_index =  (index + new) % 10
            else :
                new_index =  (index + shift) % 10
            hasil += angka[new_index]

        else:
            hasil += huruf

    return hasil


input_string = input("Masukkan string untuk dienkripsi: ")
while True:
    try:
        shift_value = int(input("Masukkan nilai pergeseran (shift): "))
        break
    except ValueError :
        print ('Input tidak valid masukkan bilangan bulat.')

encrypted_string = enkripsi(input_string, shift_value)

print("Hasil enkripsi:", encrypted_string)
