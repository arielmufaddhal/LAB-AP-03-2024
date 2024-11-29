n = list(map(int,input().split()))
genap = [i for i in n if i % 2 == 0]
jumlah_genap = sum(genap)
print(f"jumlah angka genap : {jumlah_genap}")