class Kubus:
    def __init__(self, lebar, tinggi, panjang, massa):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
        self.massa = massa

    def setlebar(self, lebar):
        self.lebar = lebar

    def getlebar(self):
        return self.lebar

    def settinggi(self, tinggi):
        self.tinggi = tinggi

    def gettinggi(self):
        return self.tinggi

    def setpanjang(self, panjang):
        self.panjang = panjang

    def getpanjang(self):
        return self.panjang

    def setmassa(self, massa):
        self.massa = massa

    def getmassa(self):
        return self.massa

    def setmassaJenis(self, massaJenis):
        self.massaJenis = massaJenis

    def getmassaJenis(self):
        return self.massa / (self.panjang * self.lebar * self.tinggi)


lebar = int(input("Masukkan lebar : "))
tinggi = int(input("Masukkan tinggi : "))
panjang = int(input("Masukkan panjang : "))
massa = int(input("Masukkan massa : "))


kubus = Kubus(lebar, tinggi, panjang, massa)
kubus.setmassa(massa)
print("Massa Jenis =", kubus.getmassaJenis())
kubus.setmassa(massa*2)
print("Massa Jenis =", kubus.getmassaJenis())

