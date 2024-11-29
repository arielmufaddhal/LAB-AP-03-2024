a = int(input("masukan jumlah data (GB): "))
b = (input("Apakah mayoritas penggunaan di jam sibuk (peak)? (y/t) "))
c = (input("Apakah anda pengguna personal atau bisnis? (p/b) "))
d = ""

if a < 10 and b == "t" and c == "p":
    d = "Paket A"
elif a < 50 and a > 10 and b == "y" and c == "p":
    d = "Paket B"
elif a > 50 and c == "y" or b == "y":
    d = "Paket C"
elif a > 50 and  b == "t" and c == "p":
    d = "Paket D"
else :
    d = "tidak ada paket yang memenuhi"

print("paket yang sesuai: " + d)