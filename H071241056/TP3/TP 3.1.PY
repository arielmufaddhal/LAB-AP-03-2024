try :
    n = int(input('Masukkan Jumlah Baris: '))
    print()

    for i in range(n):
        if i%2 == 1:
            continue
        else:
            print(' ' * (n - i) + '* ' * (i + 1))

    if n%2 == 1:  
        for i in range(n):
            if i%2 == 0:
                continue
            else:
                print(' ' * (i + 2) + '* ' * (n - i - 1))
                
    else:
        for i in range(n):
            if i%2 == 0:
                continue
            else:
                print(' ' * (i + 1) + '* ' * (n - i))
except :
    print("data tidak valid")