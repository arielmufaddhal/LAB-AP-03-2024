def berburu_harta():
    total_jarak = 0
    langkah_bahaya = False

    while True:
        try:
            langkah = int(input("Masukkan jarak langkah yang ditempuh dalam meter (0 untuk berhenti): "))
            if langkah < 0:
                print("Input tidak valid. Permainan berakhir.")
                break
            if langkah == 0:
                break
            
            if langkah > 20:
                langkah_bahaya = True
                print("Langkah lebih dari 20 meter, bahaya!")            
            total_jarak += langkah
            print(f"Total jarak: {total_jarak} meter")
        
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    if langkah_bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_jarak == 50:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

berburu_harta()
