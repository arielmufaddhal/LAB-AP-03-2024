import re
n = input("Masukkan no.telepon: ")
syarat = r"^\+62\d{8,12}$"
if re.fullmatch(syarat, n):
    print("no.telepon valid")
else:
    print("no.telepon tidak valid")