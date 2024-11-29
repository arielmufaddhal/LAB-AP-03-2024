#1
a = int(input('Masukkan panjang sisi pertama ='))
b = int(input('Masukkan panjang sisi kedua   ='))
c = int(input('Masukkan panjang sisi ketiga  ='))

if a == b == c :
    print('segitiga sama sisi')
elif a==b or b==c or c==a :
    print('Segitiga sama kaki')
elif a+b <= c or b+c <= a or c+a <= b :
    print('tidak dapat membentuk segitiga valid')
else:
    print('segitiga sembarang')

 

