try:
    import random

    def tarik_kartu():
        kartu = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  
        return random.choice(kartu)

    
    def hitung_total(kartu):
        total = sum(kartu)
        while total > 21 and 11 in kartu:
            kartu[kartu.index(11)] = 1
            total = sum(kartu)
        return total

    def mainkan_blackjack():
        print("Selamat datang di Blackjack!")
        kartu_pemain = [tarik_kartu()]
        kartu_dealer = [tarik_kartu()]
        print(f"Kartu anda: {kartu_pemain[0]}")
        print(f"Kartu dealer: {kartu_dealer[0]}")

        
        while hitung_total(kartu_pemain) <= 21:
            pilihan = input("Apakah Anda ingin mengambil kartu lagi? (y/n): ")
            if pilihan == 'y':
                kartu_pemain.append(tarik_kartu())
                print(f"Kartu anda sekarang: {hitung_total(kartu_pemain)}")
            elif pilihan == 'n':
                break
            else:
                print("Input tidak valid, silakan masukkan 'y' atau 'n'.")

        if hitung_total(kartu_pemain) > 21:
            print("Anda kalah, kartu Anda melebihi 21.")
            return

        while hitung_total(kartu_dealer) < 17:
            kartu_dealer.append(tarik_kartu())

        print(f"Kartu dealer sekarang: {hitung_total(kartu_dealer)}")

        # Menentukan pemenang
        total_pemain = hitung_total(kartu_pemain)
        total_dealer = hitung_total(kartu_dealer)
        
        if total_dealer > 21:
            print("Anda menang, dealer melebihi 21.")
        elif total_pemain > total_dealer:
            print("Anda menang!")
        elif total_pemain < total_dealer:
            print("Dealer menang!")
        else:
            print("Seri!")

    mainkan_blackjack()
except:
    print("hanya bisa memasukkan angka")