Nilai = int(input("Nilai: "))
if Nilai >= 90 and Nilai <= 100:
    print("> nilai %d = 'A'" % (Nilai))
elif Nilai < 90 and Nilai >= 80: 
    print("> nilai %d = 'B'" % (Nilai))
elif Nilai < 80 and Nilai >= 70:
    print("> nilai %d = 'C'" % (Nilai))
elif Nilai < 70 and Nilai >= 60:
    print("> nilai %d = 'D'" % (Nilai))
elif Nilai < 60 and Nilai >= 40:
    print("> nilai %d = 'E'" % (Nilai))
elif Nilai < 40 and Nilai >= 0:
    print("> nilai %d = 'F'" % (Nilai))