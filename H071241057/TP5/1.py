def palindrome(isi):   
    lawan = "".join(reversed(isi))
    tes = reversed(isi)
    print(tes)
    
    if isi == lawan :
        print("Palindrome")
    else :
        print("Not Palindrome")

isi = input("masukkan kata atau kalimat :").lower()
palindrome(isi)