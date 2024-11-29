# 1. anagram = str1 dan str2 harus memiliki frekuensi yang sama dan huruf yang sama
# 2. jika str1 dan str2 tidak sepenuhnya sama maka dilakukan penghapusan 
# 3. input str1 & str2
# 4. output jumlah yang dihapus 

def anagram (str1,str2):
    total_penghapusan = 0
    for karakter in set(str1+str2):
        total_penghapusan += abs(str1.count(karakter)- str2.count(karakter))
    

    if total_penghapusan == len(str1)+len(str2):
        print("tidak ada anagram yang dapat dihitung")
    else :
        print (f'jumlah minimum penghapusan karakter untuk membuat anagram : {total_penghapusan}')


str1 = input("masukkan str pertama = ")
str2 = input("masukkan str kedua   = ")
anagram(str1, str2)

