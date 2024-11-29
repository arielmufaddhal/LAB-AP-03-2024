def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak bisa dibagi oleh nol"
    else:
        return a / b

    
def kalkulator () :
    while True:
        try:
            a = float(input("Angka pertama:"))
            break
        except ValueError as e :
            print(f"Input tidak valid: {e}")
    
    while True:
        try:
            b = float(input("Angka kedua:"))
            break
        except ValueError as e :
            print(f"input tidak valid: {e}")
            
    operasi = input("operasi (+,-,*,/): ")
    
    if operasi=="+" :
        print(tambah(a,b))
    elif operasi=="-" :
        print(kurang(a,b))
    elif operasi=="*" :
        print(kali(a,b))
    elif operasi=="/" :
        print(bagi(a,b))
    else :
        print("Operasi tidak valid. Gunakan +,-, *, atau /.")
kalkulator()


