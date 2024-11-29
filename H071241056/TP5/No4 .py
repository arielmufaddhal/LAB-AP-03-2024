def substring(inputan):
  panjang = len(inputan)
  for i in range(1, panjang+1):
    for j in range(panjang - i + 1):
      print(inputan[j:j+i])
  
inputan = input("masukkan kata = ")
substring(inputan)