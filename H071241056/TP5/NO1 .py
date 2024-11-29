# Buatlah sebuah fungsi bernama Palindrome yang menerima sebuah string dan menentukan apakah string tersebut adalah palindrom.
# Palindrom adalah string yang serupa jika dibaca dengan urutan terbalik (Contoh : “Apa” dan “Kakak”
# Fungsi menerima memiliki 1 parameter dan akan mencetak “Palindrome” jika inputan adalah sebuah palindrome. Sebaliknya, fungsi akan mencetak “Bukan Palindrome” jika inputan bukan sebuah palindrome

def polindrom(kata):
    print(kata)
    kata = kata.replace(" ","")
    kata_balik = kata[::-1]

    return kata == kata_balik


kata = input("masukkan kata/kalimat =").lower()

if polindrom(kata):
    print("iye polindrom")

else :
    print("bukan polindrom")