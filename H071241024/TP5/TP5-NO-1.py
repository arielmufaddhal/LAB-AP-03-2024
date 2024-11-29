def Palindrome(kata):
    
    kalimat = kata
    print(kalimat[::-1])
    if kalimat == kalimat[::-1]:
        print("Palindrome")
    else:
        print("Bukan Palindrome")

kata = input("Masukkan string: ")
Palindrome(kata)