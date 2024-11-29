def anagram(x, y):
    x = sorted(x)
    y = sorted(y)
    
    v1, v2 = 0, 0 
    dihapus = 0

    while v1 < len(x) and v2 < len(y):

        if x[v1] == y[v2]:
            v1 += 1
            v2 += 1
        elif x[v1] < y[v2]:
            dihapus += 1
            v1 += 1
        else:
            dihapus += 1
            v2 += 1
    
    dihapus += len(x) - v1
    dihapus += len(y) - v2

    return dihapus

s1 = input("kata : ")
s2 = input("kata : ")
print("11">"")
print(f"huruf yang dihapus : {anagram(s1,s2)}")
