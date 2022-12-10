
x= int(input("masukkan detik: "))
jam= x/3600
c= x%3600
menit= c/60
detik= c%60

print("%02d:%02d:%02d" % (jam, menit, detik))