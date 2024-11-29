print("Selamat datang di Kalkulator sederhana!")

def kalkulator_fungsi(n, m, operasi):
    berhasil = True
    if operasi == "+":
        hasil = n + m
        print(int(hasil))

    elif operasi == "-":
        hasil = n - m
        print(int(hasil))

    elif operasi == "*":
        hasil = n * m
        print(int(hasil))

    elif operasi == "/":
        if m == 0:
            print("Pembagian dengan nol tidak diperbolehkan")
        else:
            hasil = n / m
            print(hasil)
    else:
        berhasil = False
        print("Operasi tidak valid. Gunakan +, -, *, atau /")
    return berhasil

while True :
    try:
        n = float(input("angka pertama = "))
        m = float(input("angka kedua = "))
        operasi = input("operasi = ")
        if kalkulator_fungsi(n, m, operasi):
            a = input("LANJUT? (Y): ")
            if a.lower() == "y" :
                continue
            else:
                break
        else:
            continue
            
    except:
        print("masukan bilangan kocak")
        continue
    