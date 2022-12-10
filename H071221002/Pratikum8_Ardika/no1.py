class Person :
    def __init__ (self, nama, usia, gender, asal) :
        self.name = nama
        self.age = usia
        self.IsMale = gender 
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

    def setAsal(self, asal) :
        self.asal = asal
    def cetakAsal(self) :
        print(f"Asal : {self.asal}")

    

ika = Person("Ardika", "18", "perempuan", "Soppeng")
ika.cetakName()
ika.cetakAge()
ika.cetakGender()
ika.cetakAsal()