def Palindrome(frasa):
    print(frasa[::-1]) 

    if frasa == frasa[::-1]: 
        print("merupakan palindrom")
    else:
        print("bukan kata palindrom")
frasa = input("palindrom: ")
Palindrome(frasa)
