penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB/bulan): "))
penggunaa_waktu = (input("Apakah mayoritas penggunaan diluar jam sibuk (off-peak) atau di jam sibuk (peak)?"))
jenis_pengguna = (input("Apakah Anda pengguna Personal atau Bisnis?"))

if penggunaan_data <10 and penggunaa_waktu == "off-peak" and jenis_pengguna == "personal":
    print("Paket yang cocok: Paket A")
elif (10 <= penggunaan_data <= 50 )and penggunaa_waktu == "peak" and jenis_pengguna == "personal" :
    print("Paket yang cocok: Paket B")
elif  penggunaan_data >50 and penggunaa_waktu == "peak" and jenis_pengguna == "personal" :
    print("Paket yang cocok: Paket C")
elif  penggunaan_data >50 and penggunaa_waktu == "off-peak" and jenis_pengguna == "bisnis" :
    print("Paket yang cocok: Paket D")    
else:
    print("Tidak ada paket yang cocok")

