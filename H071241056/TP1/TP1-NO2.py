#NO.2
karakter = input('masukkan karakter = ')
kalimat = input('masukkan kalimat = ')
#index 0= false, index 1=true
output = ('ditemukan dalam','tidak ditemukan dalam') [karakter not in kalimat]

print(karakter, output, '"',kalimat,'"' )
karakter = input('masukkan karakter = ')
kalimat = input('masukkan kalimat = ')
#index 0= false, index 1=true
output = ('tidak ditemukan dalam','ditemukan dalam') [karakter in kalimat]

print(karakter, output, '"',kalimat,'"' )

