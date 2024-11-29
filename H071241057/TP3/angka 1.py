while True :
     try :
          baris = int(input("Masukkan jumlah baris: "))
          break
     except ValueError :
          print ('input salah.')
line = baris//2

for i in range(line):
     a = 2*i+1
     print(" "*(line-i) + "*"*a)


for i in range(1,line):
    b = 2*(line-i-1)+1
    print(" "*(i+1) + "*"*b )
