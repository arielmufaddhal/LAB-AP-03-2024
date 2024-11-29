# # nama = 'aco'
# # nama = 'aci'


# a = 'aku'
# b = 'sigma'
# c = a+" "+b
# print(c)


# myString = 'sisfo 24'
# myLetter = myString[6]
# print(myLetter)


# # len()
# myString = 'ayam'
# print(len(myString))


# menentukan karakter pada string
# platform = "instagram"
# print(platform.find("s"))


# menemukan frekuensi dari subtstring pada string
# myString = "boooo!"
# count_string = myString.count("o")
# print(count_string)


# slicing
# a = "Abdul Lah! nibos"
# slice = a[::1]
# print(slice)


# # split
# a = "kumpul tugasta dek"
# split = a.split(" ")
# print(split)


# # startend
# a = "caracaca"
# check = a.startswith("c") or check = a.endswitch("c")
# print(check)


# # mengganti substring
# a = "abdul sangat butuh uang bos"
# z =  a.replace("sangat", "tidak") or a.replace("a", "i")
# print(z)



# a = "ayam bebek kucing"
# b = a.capitalize()
# print(b)



# reverse
# a = "ayam bebek berkelahi"
# b = reversed(a) or slice = a[::-1]
# print(''.join(b))



# a = ['ayam', 'bebek', 'ayamlagi']
# b = "_".join(a)
# print (b)



# a = input("Masukkan kata: ")
# b = a[::2]
# print(b)
# # cara agar string hanya mengambil huruf awal, akhir, dan tengah saja 

def Palindrome(kata):
    
    kalimat = kata.lower()
    
    if kalimat == kalimat[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

kata = input("Masukkan kata: ")
Palindrome(kata)




def acronym(kalimat):
    return ''.join(kata[0].upper() for kata in kalimat.split())

kalimat = input("Masukkan kalimat: ")
hasil = acronym(kalimat)
print(hasil)




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




def substring(kata):
    panjang_kata = len(kata)
    
    for panjang in range(1, panjang_kata + 1):
        for jumlah_kata in range(panjang_kata - panjang + 1):
            substring = kata[jumlah_kata:jumlah_kata + panjang]
            print(substring)

input_kata = input("Masukkan sebuah string: ")
substring(input_kata)





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
        else:
            hasil += huruf

    return hasil

teks_awal = input("Masukkan String: ")
while True:
    try:
        pergeseran = int(input("Masukkan jumlah pergeseran: "))
        break
    except ValueError:
        print("Masukkan Angka yang benar")

hasil_enkripsi = pergeseran_karakter(teks_awal, pergeseran)

print(f"Text : {teks_awal}")
print(f"Shift : {pergeseran}")
print(f"Cipher: {hasil_enkripsi}")