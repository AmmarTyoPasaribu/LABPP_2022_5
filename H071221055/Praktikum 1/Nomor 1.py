import math
h = float(input("Masukkan Ketinggian Menara (dalam satuan meter): "))
a = float(input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal: "))
b = float(input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal: "))

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan
z = round(panjang, 1)
print("Panjang Kapalnya adalah", z, "m")
