def langkah(): 
    bahaya = "tidak"
    total = 0
    while True:
        try:
            langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
            if langkah == 0 :
                break
            elif 0 < langkah <= 20:
                total += langkah
            else:
                total += langkah
                bahaya = "ya"
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat")
            continue
    print(f"Total jarak: {total} meter")
    print(f"Ada bahaya: {bahaya}")
    if bahaya == "ya" :
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total == 50:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    elif total != 50:
        print("Keputusan: Tidak menemukan harta karun. Coba lagi!")
langkah()