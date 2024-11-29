#4
data = int(input('Masukkan data yang digunakan (GB) = '))
waktu = input("Apakah penggunaan peak/off peak? = ").lower()
jenis = input('Apakah anda pengguna Personal/Bisnis? = ').lower()


if data < 10 and waktu == "off peak" and jenis == "personal" :
    print('Paket yang sesuai : Paket A')
elif 10 <= data <= 50 and waktu == "peak" and jenis == "personal":
    print('Paket yang sesuai : Paket B')
elif data > 50 :
    if waktu == "peak" and (jenis == "personal" or jenis == "bisnis") :
       print('Paket yang sesuai : Paket C')
    if waktu == "off peak" and jenis == "bisnis":
       print('Paket yang sesuai : Paket D')
else:
    print('Tidak ada paket yang cocok')
    