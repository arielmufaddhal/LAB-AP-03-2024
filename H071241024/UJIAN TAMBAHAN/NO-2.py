from itertools import permutations
n = input()
permutasi = sorted(set(["".join(i) for i in permutations(n)]))
print(permutasi)