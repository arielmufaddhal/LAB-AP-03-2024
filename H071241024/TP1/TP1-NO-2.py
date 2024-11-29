Karakter = input('Masukkan Karakter : ')
Kalimat = input('Masukkan Kalimat : ')

print (f'"{Karakter}" tidak ditemukan dalam "{Kalimat}"'* (Karakter not in Kalimat)+ f'"{Karakter}" ditemukan dalam "{Kalimat}"'* (Karakter in Kalimat))