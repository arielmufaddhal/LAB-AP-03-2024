def hitung_langkah(n):

    n=float(n)
    langkah = 0
    while n != 1:
        if n % 2 == 0 :
            n/=2
            print(n)
            langkah+=1
        else :
            n= n*3+1
            print(n)
            langkah+=1
    return langkah

while True :
    try:
        n = int(input("Masukkan bilangan bulat positif: "))
        if  n <= 0 :
           raise ValueError
        else :
            break
    except ValueError:
        print("Input tidak Valid, masukkan hanya angka bulat yang lebih dari 1")


hasil = hitung_langkah(n)
print(f"Jumlah langkah: {hasil}")
