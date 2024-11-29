import re

def ipv4(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$'
    return bool(re.match(pattern, ip))

def ipv6(ip):
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(pattern, ip))

def validate_ip(ip):
    ip = ip.strip()
    
    if len(ip) > 500:
        return "Bukan IP Address"
    if ipv4(ip):
        return "IPv4"
    if ipv6(ip):
        return "IPv6"
    return "Bukan IP Address"

def main():   
    while True:
        try:
            N = int(input())
            break
        except ValueError:
            print("Input hanya angka bulat")

    for _ in range(N):
        ip = input()
        result = validate_ip(ip)
        print(result)

main()