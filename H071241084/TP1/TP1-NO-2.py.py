karakter = input("masukkan karakter:")
kalimat = input("masukkan kalimat:")
pesan = ["tidak ditemukan dalam","merupakan bagian dari"][karakter in kalimat]
print(f"'{karakter}' {pesan} '{kalimat}'")