try:
    usia = int(input("Masukkan usia: "))
    if usia < 0:
        print("usia tidak valid")
    elif usia < 12:
        print("anak-anak")
    elif 12 <= usia <= 17:
        print("remaja")
    elif 18 <= usia <= 64:
        print("dewasa")
    else:
        print("lansia")
except ValueError:
    print("hanya angka")