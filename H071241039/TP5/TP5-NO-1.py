kata = input("masukkan string: ")

def palindrom(kata):
    print(kata[::-2])  
    if kata == kata[::-2]:
        print(f"{kata} adalah Palindrom")
    else:
        print(f"{kata} bukan Palindrom")

palindrom(kata)
