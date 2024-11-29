detik = int(input("Masukkan jumlah detik: "))

jam = detik // 3600
detik %= 3600
menit = detik // 60
detik %= 60

print(f"{jam:02}:{menit:02}:{detik:02}")
