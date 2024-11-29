penggunaan_data = (input("Masukkan jumlah data yang digunakan (GB) :"))
waktu_penggunaan = (input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? :"))
jenis_pengguna = (input("Apakah anda pengguna personal atau bisnis? :"))

if int(penggunaan_data) < 10:
    penggunaan = "Ringan"
elif 10 <= int(penggunaan_data) <= 50:
    penggunaan = "Sedang"
else:
    penggunaan = "Berat"



if penggunaan == "Ringan" and waktu_penggunaan == "off-peak" and jenis_pengguna == "personal":
    print("Paket A") 
elif penggunaan == "Sedang" and waktu_penggunaan == "peak" and jenis_pengguna == "personal":
    print("Paket B") 
elif penggunaan == "Berat" and waktu_penggunaan == "peak":
    print("Paket C") 
elif penggunaan == "Berat" and waktu_penggunaan == "off-peak" and jenis_pengguna == "Bisnis":
    print("Paket D") 
else:
    print("Tidak ada paket yang cocok")

print("Paket yang cocok:")