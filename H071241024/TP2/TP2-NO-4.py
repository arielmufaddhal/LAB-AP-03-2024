JumlahData = int(input("Masukkan jumlah data yang digunakan (GB): "))
WaktuPenggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? " ).lower()
JenisPengguna = input("Apakah anda pengguna personal atau bisnis? ").lower()

if JumlahData < 10 and WaktuPenggunaan == "off-peak" and JenisPengguna == "personal":
    Paket = "PaketA"
elif 10 <= JumlahData <= 50 and WaktuPenggunaan == "peak" and JenisPengguna == "personal":
    Paket = "PaketB"
elif JumlahData > 50 and WaktuPenggunaan == "peak" and JenisPengguna == ("personal" or "bisnis"):
    Paket = "PaketC"
elif JumlahData > 50 and WaktuPenggunaan == "off-peak" and JenisPengguna == "bisnis":
    Paket = "PaketD"
else:
    Paket = "Tidak ada paket yang cocok"

print (f'Paket yang sesuai: {Paket}')