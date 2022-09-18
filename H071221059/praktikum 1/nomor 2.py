detik = int(input("masukkan jumlah detik yang ingin dihitung: "))

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik1 = sisa_detik % 60 

print("%d:%02d:%02d" % (jam, menit, detik1))