import random

def AmbilKartu():
  return random.randint(1, 11)

def TotalKartu(kartu):
  return sum(kartu) 

def KartuYangDitampilkan(pemain, kartu):
  print(f'kartu {pemain} sekarang adalah: {TotalKartu(kartu)}')
  
def GiliranPemain():
  KartuPemain = [AmbilKartu()]
  while True:
    KartuYangDitampilkan("anda", KartuPemain)
    pilihan = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
    if pilihan == "y":
      KartuPemain.append(AmbilKartu()) 
      if TotalKartu(KartuPemain) > 21:
        KartuYangDitampilkan("anda", KartuPemain)
        print("Anda kalah, kartu anda melebihi 21.")
        return None
    elif pilihan == "n":
      return KartuPemain
    else:
      print("gunakan y/n")
      
def GiliranDealer(KartuDealer):
  print(f"\nKartu dealer adalah {TotalKartu(KartuDealer)}")
  while TotalKartu(KartuDealer) < 17:
    KartuDealer.append(AmbilKartu())
    print(f'Kartu dealer sekarang adalah: {TotalKartu(KartuDealer)}')
  return KartuDealer

def Pemenang(KartuPemain, KartuDealer):
  TotalKartuPemain = TotalKartu(KartuPemain)
  TotalKartuDealer = TotalKartu(KartuDealer)
  
  if TotalKartuDealer > 21:
    print("Anda menang, dealer melebihi 21.")
  elif TotalKartuPemain > TotalKartuDealer:
    print("Anda menang!")
  elif TotalKartuPemain == TotalKartuDealer:
    print("Seri!")
  else:
    print("Dealer menang!")
    
def mulai():
  print("Welcome to BlackJack!")
  KartuPemain = GiliranPemain()
  if KartuPemain is None:
    return
  
  KartuDealer = [AmbilKartu()]
  KartuDealer = GiliranDealer(KartuDealer)
  
  Pemenang(KartuPemain, KartuDealer)
    
mulai()