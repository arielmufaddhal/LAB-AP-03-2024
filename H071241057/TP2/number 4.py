data = float(input("Masukkan penggunaan data per bulan (dalam GB): "))
waktu = input("Mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk(peak): ").lower()
penggunaan = input("Jenis pengguna (personal/bisnis): ")

if data < 10 and waktu == "off-peak" and penggunaan == "personal":
    print("Paket yang sesuai adalah: Paket A")
elif 10 <= data <= 50 and waktu == "peak" and penggunaan == "personal":
    print("Paket yang sesuai adalah: Paket B")
elif data > 50 and waktu == "peak" and (penggunaan == "personal" or penggunaan == "bisnis"):
    print("Paket yang sesuai adalah: Paket C")
elif data > 50 and waktu == "off-peak" and penggunaan == "bisnis":
    print("Paket yang sesuai adalah: Paket D")
else:
    print("Tidak ada paket yang sesuai")
