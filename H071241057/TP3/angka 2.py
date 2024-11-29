import random
angka = random.randint(1,100)
n=1
while n<=5:
    while True :
        try :
            tebak = int(input("tebakan anda :"))
            n+=1
            break
        except ValueError :
            print ("input tidak valid.")

    if tebak == 0 :
        break
    elif tebak > angka :
        print("angka terlalu besar.")
    elif tebak < angka :
        print("angka terlalu kecil.")
    elif tebak == angka :
        print("SELAMAT KAMU MENANG!!!")
        break
   
print (f"angka yang benar {angka}")

