def jumlah_penghapusan(string1, string2):
    frekuensi = {}

    for karakter in string1:
        frekuensi[karakter] = frekuensi.get(karakter, 0) + 1
    for karakter in string2:
        frekuensi[karakter] = frekuensi.get(karakter, 0) - 1

    total_hapus = sum(abs(count) for count in frekuensi.values())
    
    return total_hapus

string1 = input("Masukkan string pertama: ")
string2 = input("Masukkan string kedua: ")
hasil = jumlah_penghapusan(string1, string2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")