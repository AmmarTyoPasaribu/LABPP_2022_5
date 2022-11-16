class Kubus :
    def __init__(self, lebar, tinggi, panjang) :
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang 

    def setMassa(self, massa) :
        self.massa = massa

    def getMassaJenis (self) :
        self.volume = self.panjang * self.lebar * self.tinggi 
        self.MassaJenis = self.massa / self.volume
        return self.MassaJenis

lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

Kubus = Kubus(lebar, tinggi, panjang)

Kubus.setMassa(massa)
print("Massa Jenis =", Kubus.getMassaJenis())

Kubus.setMassa(massa*2)
print("Massa Jenis =", Kubus.getMassaJenis())