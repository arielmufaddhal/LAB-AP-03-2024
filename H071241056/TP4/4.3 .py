def hitung_langkah(n):
    if n == int or n>1 :
        langkah=0
        while n != 1 :
            if n%2 == 0 :
                n = n//2
                print(float(n))
            else :
                n = n*3+1
                print(float(n))
            langkah += 1
        print(f"banyak langkah= {langkah}")
    elif n==1 :
        print("kalau 1 langkahnya 0 dong kak")
    else :
        print("yang bilangan positif-positif aja")
try :
    n = int(input("masukkan angka = "))
    hitung_langkah(n)
except :
    print("masukkan angka kak")