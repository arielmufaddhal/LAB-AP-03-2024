def UrutanPembagian(angka):
    urutan = []
    while angka != 1:
        if angka % 2 == 0:
            angka = angka / 2
        else:
            angka = angka * 3 + 1
        urutan.append(angka)
       
    return urutan

def mulai():
    try:
        angka = int(input("Masukkan angka: "))
        if angka <= 0:
            raise ValueError
    except ValueError:
        print("Input tidak Valid")
        return
    
    urutan = UrutanPembagian(angka)
    
    for nilai in urutan:
        print(f"{float(nilai)}")
    
    print(f'Jumlah langkah: {len(urutan)}')#menghitung total langkah dari urutan
    
mulai()