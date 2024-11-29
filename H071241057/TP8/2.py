import re

def ipv4(ip):
    pattern = r"^(\d{1,3}[.]){3}\d{1,3}$"

    if re.match(pattern, ip):
        angka = ip.split('.')
        for i in angka:
            if (0 <= int(i) <= 255):
                return True
        return False
    return False

def ipv6(ip):
    ipv6_pattern = r"^([0-9a-fA-F]{1,4}[:]){7}[0-9a-fA-F]{1,4}$"

    if re.match(ipv6_pattern, ip):
        return True
    return False

while True:
    try :
        N = int(input("Masukkan jumlah baris inputan: "))
        break
    except ValueError:
        print ("input hanya angka")

for i in range(N):
    ip= input().strip()
    
    if ipv4(ip):
        print ("IPv4")
    elif ipv6(ip):
        print ("IPv6")
    else:
        print ("Bukan IP Address")
