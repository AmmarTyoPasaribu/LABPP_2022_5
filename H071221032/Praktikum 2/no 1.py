x = int(input("Masukkan angka: "))

if x >= 90 and x <= 100:
    y = "A"
elif x >= 80:
    y = "B"
elif x >= 70:
    y = "C"
elif x >= 60:
    y = "D"
elif x >= 40:
    y = "E"
elif x >= 0 and x < 40:
    y = "F"

print("Nilai", x, "=", y)