print("Konverensi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
Celcius = int(input("Masukan Suhu dalam Celcius : "))

Kelvin = Celcius + 273
Reamur = 4/5 * Celcius
Fahrenheit = (9/5 * Celcius) + 32

print ("hasil konverensi dari suhu %d ke Kelvin adalah : %d" % (Celcius, Kelvin))
print ("hasil konverensi dari suhu %d ke Reamur adalah : %d" % (Celcius, Reamur))
print ("hasil konverensi dari suhu %d ke Fahrenheit adalah : %d" % (Celcius, Fahrenheit))