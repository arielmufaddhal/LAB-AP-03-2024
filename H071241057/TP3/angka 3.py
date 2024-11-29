while True:
    try:
        N = int(input("Masukkan angka: "))
        break 
    except ValueError:
        print("Input salah, masukkan angka bulat saja")
        
while True:
    try:
        M = int(input("Masukkan angka: "))
        break 
    except ValueError:
        print("Input salah, masukkan angka bulat saja")

for x in range(0,N): 
    for y in range (0,M): 
        print(f"MOVE to ({x},{y})")