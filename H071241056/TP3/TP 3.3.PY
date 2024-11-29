n = int(input("Masukkan jumlah baris (N): ")) 
m = int(input("Masukkan jumlah kolom (M): ")) 
 
for i in range(n): 
    if i % 2 == 0: 
        for j in range(m): 
            print(f"MOVE ke ({i}, {j})") 
    else: 
        for j in range(m - 1, -1, -1): 
            print(f"MOVE ke ({i}, {j})")