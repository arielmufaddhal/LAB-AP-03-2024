def perhitungan(a, b, operasi):
    if operasi == "+":
        return a + b
    elif operasi == "-":
        return a - b
    elif operasi == "*":
        return a * b
    elif operasi == "/":
        if b == 0:
            return "Pembagian dengan nol tidak diperbolehkan."
        else:
            return a / b 
    else:
        return "Operasi tidak valid. Gunakan +, -, *, atau /."
    
def MemintaAngka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError as huruf:
            print(f"Input tidak valid: {huruf}")
            
def MemintaOprasi():
    while True:
            operasi = input("Operasi (+,-,*,/): ")
            if operasi in ["+", "*", "/", "-" ]:
                return operasi
                break
            else:
               print( "Input tidak valid: " + operasi)
               continue
                
            
            
def mulai():
    print("Selamat datang di Kalkulator Sederhana!")
    a = MemintaAngka("Angka pertama: ")
    b = MemintaAngka("Angka kedua: ")
    operasi = MemintaOprasi()

    hasil = perhitungan(a, b, operasi)
    
    if isinstance(hasil, str):
        print(hasil)
    elif hasil.is_integer():
        print(f'Hasil: {int(hasil)}')
    else:
        print(f"Hasil: {hasil}")
          
mulai()