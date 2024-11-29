import random

def tarik_kartu():
    return random.randint(1, 11)

def hitung_nilai(kartu):
    return sum(kartu)

def blackjack():
    print("Selamat datang di Blackjack!")
    
    kartu_pemain = [tarik_kartu()]
    kartu_dealer = [tarik_kartu()]
    
    while True:
        print(f"Kartu anda sekarang adalah: {kartu_pemain}, total: {hitung_nilai(kartu_pemain)}")
        aksi = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        
        if aksi == 'y':
            kartu_pemain.append(tarik_kartu())
            if hitung_nilai(kartu_pemain) > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif aksi == 'n':
            break
        else :
            print("Masukkan input y/n.")
    
    print(f"Kartu dealer adalah: {kartu_dealer}, total: {hitung_nilai(kartu_dealer)}")
    
    while hitung_nilai(kartu_dealer) < 17:
        kartu_dealer.append(tarik_kartu())
    
    nilai_pemain = hitung_nilai(kartu_pemain)
    nilai_dealer = hitung_nilai(kartu_dealer)

    print(f"Kartu dealer sekarang adalah: {kartu_dealer}, total: {nilai_dealer}")

    if nilai_dealer > 21:
        print("Anda menang, dealer melebihi 21.")
    elif nilai_pemain > nilai_dealer:
        print("Anda menang!")
    elif nilai_pemain < nilai_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

blackjack()
