import re

def valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return re.search(pattern, username)

def valid_email(email):
    pattern = r"^[a-z]+\d{2,}@[a-z]+\.(com|co\.id)$"
    return re.search(pattern, email)

def valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]{8,}$"
    return re.search(pattern, password)

username = input("Masukkan username: ")
if valid_username(username):
    email = input("Masukkan email: ")
    if valid_email(email):
        password = input("Masukkan password: ")
        if valid_password(password):
            print(f"\nRegistrasi berhasil! Selamat datang, {username}!")
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal!")
    else:
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")