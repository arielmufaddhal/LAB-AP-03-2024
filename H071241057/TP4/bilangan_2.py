def harta ():
    bahaya = 0
    jarak = 0
    while True :
        try :
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai : "))
            if langkah <= 0 :
                break
            elif langkah > 20 :
                bahaya = 1
                
            jarak+=langkah
            if jarak >= 5000:
                break


        except ValueError :
            print ('Input tidak valid masukkan bilangan bulat.')
    
    print (f"Total jarak : {jarak} meter")

    if bahaya == 1 :
        print ("Ada bahaya: ya")
        print ("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi! ")
    elif jarak == 50 and bahaya == 0 :
        print ("Ada bahaya: tidak")
        print ("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang! ")
    else : 
        print ("Ada bahaya: Tidak")
        print ("Keputusan: Tidak menemukan harta karun. Coba lagi!")

harta()
