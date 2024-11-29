import random

# Fungsi untuk membuat dek kartu dan mengacaknya
def create_deck():
    # Nilai kartu: angka 2-10, kartu wajah (J, Q, K), dan Ace (A)
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    suits = ['Hati', 'Sekop', 'Keriting', 'Wajik']  # Jenis kartu
    # Dek kartu dengan list comprehension
    deck = [(v, s) for v in values for s in suits]
    random.shuffle(deck)  # Mengocok dek
    return deck, values

print

# Fungsi untuk menghitung total nilai kartu di tangan
def calculate_hand_value(hand, values):
    value = sum(values[card[0]] for card in hand)
    # Tangani Ace (A bisa bernilai 1 atau 11)
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10  # Kurangi 10 jika ada Ace dan nilai total melebihi 21
        num_aces -= 1
    return value

# Fungsi utama untuk menjalankan permainan blackjack
def blackjack_game():
    print("Welcome to Blackjack!")
    deck, values = create_deck()  # Membuat dan mengacak dek kartu

    # Kartu awal untuk pemain dan dealer
    player_hand = [deck.pop()]
    dealer_hand = [deck.pop()]

    print(f"Kartu anda sekarang adalah: {player_hand}")
    print(f"Kartu dealer adalah: {dealer_hand[0]}")  # Tampilkan satu kartu dealer

    # Giliran pemain
    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        if choice == 'y':
            player_hand.append(deck.pop())  # Ambil kartu tambahan
            player_value = calculate_hand_value(player_hand, values)  # Hitung nilai kartu pemain
            print(f"Kartu anda sekarang adalah: {player_hand}")
            if player_value > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return  # Permainan berakhir jika pemain kalah
        else:
            break  # Pemain berhenti mengambil kartu

    # Giliran dealer
    print(f"Kartu dealer sekarang adalah: {dealer_hand}")
    while calculate_hand_value(dealer_hand, values) < 17:
        dealer_hand.append(deck.pop())  # Dealer mengambil kartu sampai nilainya >= 17
        print(f"Kartu dealer sekarang adalah: {dealer_hand}")

    # Hitung nilai akhir pemain dan dealer
    player_value = calculate_hand_value(player_hand, values)
    dealer_value = calculate_hand_value(dealer_hand, values)

    # Tentukan pemenang
    if dealer_value > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player_value > dealer_value:
        print("Anda menang!")
    elif player_value == dealer_value:
        print("Seri!")
    else:
        print("Dealer menang!")

# Memulai permainan blackjack
blackjack_game()

