#Pola bintang
n = "0"
try:
    n = int(input("Masukkan jumlah baris: "))
except:
    n = int(n)
finally :
    if n > 0:
      for i in range(1, n+1):
         if i % 2 == 1:
            print(" " * (n - i), end = " ")
            print("#" * (2 * i - 1))
      for i in range(n-1, 0, -1):
         if i % 2 == 1:
            print(" " * (n - i), end = " ")
            print("#" * (2 * i - 1))
    else : 
       print("input tidak tepat")


