def LangkahYangAman(langkah):
    return langkah <= 20

def LetakHartaKarun(jarak):
    return jarak == 50

def penginputan():
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: ")) 
            if langkah < 0:
                print("Masukkan bil bulat positif")
            else:
                return langkah
        except ValueError:
            print("Input tidak valid. Masukkan angka bulat.")
            
def mulai():
    jarak = 0
    aman = True
    
    while True:
        langkah = penginputan()
        if langkah == 0:
            break
        if not LangkahYangAman(langkah):
            aman = False
            
        jarak += langkah
        print(f'Total jarak: {jarak}')
        
    print(f'Total jarak: {jarak} meter')
    print(f'Ada bahaya: {"Tidak" if aman else "Ya"}')
    
    if not aman:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba Lagi!")
    elif LetakHartaKarun(jarak):
        print("Keputusan: Aman! kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")
        
mulai()