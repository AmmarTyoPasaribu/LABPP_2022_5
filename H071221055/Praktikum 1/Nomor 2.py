print("Konversi Detik ke Jam")
nilai = int(input("Masukkan detik : "))

jam = nilai // 3600
sisadetik = nilai % 3600

menit = sisadetik // 60
detik = sisadetik % 60

print("%02d:%02d:%02d" % (jam, menit, detik))
