class Kubus:
    def __init__(self, lebar: float, tinggi: float, panjang: float, massa = float(), massaJenis = float()):
        self.lebar = lebar
        self.tinggi = tinggi
        self.panjang = panjang
    
    def setLebar(self, lebar: float):
        self.lebar = lebar

    def setTinggi(self, tinggi: float):
        self.tinggi = tinggi

    def setPanjang(self, panjang: float):
        self.panjang = panjang

    def setMassa(self, massa: float):
        self.massa = massa

    def getMassaJenis(self):
        sum = self.massa / (self.lebar * self.tinggi * self.panjang)
        self.massaJenis = sum
        return sum
    
### POTONGAN PROGRAM ###
lebar = float(input())
tinggi = float(input())
panjang = float(input())
massa = float(input())

kubus = Kubus(lebar, tinggi, panjang)

kubus.setMassa(massa)
print("Massa Jenis =", kubus.getMassaJenis())

kubus.setMassa(massa*2)
print("Massa Jenis =", kubus.getMassaJenis())
### END OF POTONGAN PROGRAM ###