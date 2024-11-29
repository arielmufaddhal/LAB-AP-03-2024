def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    try:
        angka1 = float(input("Angka pertama: "))
        angka2 = float(input("Angka kedua: "))
        operasi = input("Operasi (+, -, *, /): ")

        if operasi == '+':
            hasil = angka1 + angka2
        elif operasi == '-':
            hasil = angka1 - angka2
        elif operasi == '*':
            hasil = angka1 * angka2
        elif operasi == '/':
            if angka2 != 0:
                hasil = angka1 / angka2
            else:
                return "Pembagian dengan nol tidak diperbolehkan."
        else:
            return "Operasi tidak valid. Gunakan +, -, *, atau /."

        return f"Hasil: {hasil}"

    except ValueError as e:
        return f"Input tidak valid: {e}"

print(kalkulator())
