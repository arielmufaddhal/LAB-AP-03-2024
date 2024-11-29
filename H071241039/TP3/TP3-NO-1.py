try:
    baris = int(input("Masukan jumlah baris: "))
    for i in range (1, (baris // 2) + 2):
        print(((baris // 2) + 1 - i) * " " + (2*i-1) * "*")
    if baris % 2 == 0:
        print ("*" * (baris + 1))
    for i in range ((baris // 2), 0, -1):
        print(((baris // 2) + 1 - i)* " " + (2*i-1) * "*")
          
except:
    print("data tidak valid")
