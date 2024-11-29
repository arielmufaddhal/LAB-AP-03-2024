def substring(kata):
    panjang_kata = len(kata)
    
    for panjang in range(1, panjang_kata + 1):
        for jumlah_kata in range(panjang_kata - panjang + 1):
            substring = kata[jumlah_kata:jumlah_kata + panjang]
            print(substring)

input_kata = input("Masukkan sebuah string: ")
substring(input_kata)