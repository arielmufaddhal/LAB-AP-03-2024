# 1. saya melangkah 
# 2. jika langkah saya kurang dari 20 saya tidak menemukan harta karun
# 3. jika langkah saya melebihi 20 saya tidak aman 
# 4. saat langkah saya totalnya 50 pas maka saya berhasil menemukan harta karun
# 5. deteksi bahaya (>20 dan >50) tidak menggali 
# 6. 0 dan bil negatif berarti berhenti 
# 7. outputan total langkah, bahaya, keputusan 

def harta_karun():
    total_langkah = 0
    bahaya = False
    while True :
        langkah = input("Masukkan langkah (meter) atau 0 untuk berhenti = ")

        if langkah == "0" :
            break
        
        try :
            langkah = int(langkah)       
            if langkah <=0:
                break

            total_langkah+= langkah
            if total_langkah > 20 :
                bahaya = True
     
        except :
            print("Input tidak valid, masukkan bilangan bulat positif ")
    
    print("total langkah =",total_langkah)
    if total_langkah == 50 :
        print("ada bahaya = tidak")
        print("Aman! kamu tepat menemukan harta karun dan menang")
    elif bahaya == True :
        print("ada bahaya = ya")
        print("Keputusan : tidak aman untuk menggali. coba lagi!")
    else :
        print("Tidak menemukan harta karun. Coba lagi!")

harta_karun()