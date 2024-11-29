try:
    n = int(input("Masukkan jumlah baris: "))
 
 #bagian atas   
    if n > 0:
        for i in range((n+1)//2):
            for j in range((n - 1)//2 -i):
             print(' ', end=" ")

        for q in range (2*i+1):
            print('*', end=" ")
        print()

# Bagian bawah
    for i in range((n//2)-1,-1,-1):
        for j in range ((n - 1)// 2 - i):
            print(' ', end=" ")

        for q in range (2*i+1):
            print('*', end=" ")
        print()

except:
    print("angka bukanlah bilangan bulat")

  
    


        