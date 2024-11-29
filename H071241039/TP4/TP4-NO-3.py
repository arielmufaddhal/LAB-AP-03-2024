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
        print("jangan 1 nanti langkahnya 0 hmzzzz")
    else :
        print("masukin bilangan positif kaksssss")
try :
    n = int(input("masukkan angka = "))
    hitung_langkah(n)
except :
    print("masukkan angka heyy")

