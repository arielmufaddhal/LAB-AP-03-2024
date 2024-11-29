while True :
    try :
        A = int(input("masukkan populasi awal serangga A : "))
        B = int(input("masukkan populasi awal serangga B : "))
        hari = int(input("masukkan jumlah hari : "))
        break
    except ValueError :
        print ("input salah, masukkan kembali")
    



for i in range (1,hari+1) :
    if i % 2 == 1 :
        A = (A*130)//100
        B = (B*150)//100
    else :
        A = (A*80)//100
        B = (B*60)//100
    
    if i % 5 == 0 :
        print(f"Hari {i}: Predator memakan 10% populasi.")
        A = (A*90)//100
        B = (B*90)//100

    print(f"Hari {i}: Serangga A = {A}, Serangga B = {B}")

