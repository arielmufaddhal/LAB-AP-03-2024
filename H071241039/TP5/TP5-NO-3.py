def jumlah_penghapusan(str1, str2):
    frekuensi = {}
    for karakter in str1:
        frekuensi[karakter] = frekuensi.get(karakter, 0) + 1
    for karakter in str2:
        frekuensi[karakter] = frekuensi.get(karakter, 0) - 1
    total_hapus = sum(abs(count) for count in frekuensi.values())
    
    return total_hapus

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")
hasil = jumlah_penghapusan(str1, str2)
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")

