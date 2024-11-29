try : 
    N = int(input("Masukkan jumlah baris (N): "))
    M = int(input("Masukkan jumlah kolom (M): "))

# posisi awal 
    baris = 0
    kolom = 0

# mengontrol pergerakan robot
    while baris < N:
    # Bergerak ke kanan sampai ujung baris
        while kolom < M:
            print(f"MOVE to ({baris},{kolom})")
            kolom += 1

    # Turun satu baris
    baris += 1

    # Jika bukan baris terakhir, bergerak ke kiri sampai awal baris
    if baris < N:
        kolom -= 1
        while kolom >= 0:
            print(f"MOVE to ({baris},{kolom})")
            kolom -= 1

        # Siapkan untuk bergerak ke kanan pada baris berikutnya
        kolom += 1
except: 
    print("masukkan angka")
        
