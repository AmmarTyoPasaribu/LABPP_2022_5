class Person :
    def __init__ (self, nama, usia, gender, tinggi, prodi, alamat, asal) :
        self.name = nama
        self.age = usia
        self.IsMale = gender 
        self.tinggi = tinggi
        self.prodi = prodi
        self.alamat  = alamat
        self.asal = asal

    def setName(self, nama) :
        self.name = nama 
    def cetakName(self) :
        print(f"Nama : {self.name}")

    def setAge(self, usia) :
        self.age = usia 
    def cetakAge(self) :
        print(f"Umur : {self.age}")

    def setGender(self, gender) :
        self.IsMale = gender 
    def cetakGender(self) :
        if self.IsMale == True :
            print("Gender : Laki-laki")
        else : 
            self.IsMale == False
            print("Gender : Perempuan")

    def setTinggi(self, tinggi) :
        self.tinggi = tinggi
    def cetakTinggi(self) :
        print(f"Tinggi badan : {self.tinggi}")

    def setProdi(self, prodi) :
        self.prodi = prodi 
    def cetakProdi(self) :
        print(f"Prodi : {self.prodi}")

    def setAlamat(self, alamat) :
        self.alamat = alamat
    def cetakAlamat(self) :
        print(f"Alamat : {self.alamat}")

    def setAsal(self, asal) :
        self.asal = asal
    def cetakAsal(self) :
        print(f"Asal : {self.asal}")

    

elva = Person("Elva Aprili Timang", 18, False, "150 cm", "Jl. Sahabat 1", "Sistem Informasi", "Luwu Timur") # membuat objek Person bernama Elva
elva.cetakName()
elva.cetakAge()
elva.cetakGender()
elva.cetakTinggi()
elva.cetakProdi()
elva.cetakAlamat()
elva.cetakAsal()