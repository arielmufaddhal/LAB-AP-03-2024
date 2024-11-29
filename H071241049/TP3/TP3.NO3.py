#Robot
N = int(input("Masukkan jumlah baris (N): "))
M = int(input("Masukkan jumlah kolom (M): "))

baris = 0
kolom = 0

while baris < N:
    while kolom < M:
        print(f"MOVE to ({baris},{kolom})")
        kolom += 1

    baris += 1

    if baris < N:
        kolom -= 1
        while kolom >= 0:
            print(f"MOVE to ({baris},{kolom})")
            kolom -= 1
       
    kolom += 1