suhu_celcius = int(input("Masukkan suhu dalam celcius:"))
suhu_kelvin = suhu_celcius + 273.15
suhu_reamur = suhu_celcius * 4 / 5
suhu_fahrenheit = (suhu_celcius * 9 / 5) + 32

print(f"suhu dalam kelvin: {suhu_kelvin:.2f} K")
print(f"suhu dalam reamur: {suhu_reamur:.2f} Re")
print(f"suhu dalam fahrenheit: {suhu_fahrenheit:.2f} F")