#NO.3 Conversi detik ke jam

detik = int(input('masukkan jumlah detik = '))
jam = detik//3600
sisa_detik_menit = detik % 3600
 
menit = sisa_detik_menit // 60
sisa_detik_detik = sisa_detik_menit % 60

print(f'{jam:02}:{menit:02}:{sisa_detik_detik:02}')