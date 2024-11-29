import random

def kartu():
    return random.randint(1,11)

def  blackjack ():
    player = kartu()
    print (f"kartu anda sekarang adalah {player}")

    while True:

        n = str(input(f"apakah anda ingin menambah kartu? (y/n) : \n")).lower()
        
        if n == "y" :
            baru = kartu()
            player+=baru
            print (f"kartu anda sekarang adalah {player}")
        elif n == "n":
            break
        else :
            print('input salah, masukkan hanya "y" atau "n".')

        if player >21 :
            print ("Anda kalah, kartu anda melebihi 21")
            break
        
    while True :
        if player >21 :
             break
        elif player <=21 :
            dealer = kartu()
            print (f"kartu dealer adalah {dealer}")

            while dealer <= 17 :
                baru1= kartu()
                dealer+=baru1
                print (f"kartu dealer sekarang adalah {dealer}")
            
            if player > dealer :
                print ("kamu menang!!")
            elif player < dealer :
                print ("kamu kalah.")
            elif player == dealer :
                print ("seri.")    
            break

print("Welcome to Blackjack!")

blackjack()


    

        
       
    

