print("---Konversi detik---")

detik = int(input("Masukkan detik: "))

menit = 0
jam = 0

#menghitung jam
while detik >= 3600:
    detik = detik - 3600
    jam = jam + 1

#menghitung menit
while detik >= 60:
    detik = detik - 60
    menit = menit + 1

#print(f"{jam:02d}:"+f"{menit:02d}:"+f"{detik:02d}")
print("%02d:%02d:%02d" % (jam,menit,detik))
