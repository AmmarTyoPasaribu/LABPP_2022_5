while True:
    derajat = float(input(""))
    waktu = (1/15) * 3600 * derajat
    jam = waktu / 3600  
    c = waktu % 3600
    menit = c / 60
    detik = c % 60
    jam_ = (jam + 6) % 24
    if jam_>=0 and jam_<=11: 
        print("Selamat Pagi!")
    if jam_>11 and jam_<=15: 
        print("Selamat Siang!")
    if jam_>15 and jam_<=18: 
        print("Selamat Sore!")
    if jam_>18 and jam_<=24: 
        print("Selamat Malam!")    
    print("%02d:%02d:%02d" % (jam_, menit, detik))
        