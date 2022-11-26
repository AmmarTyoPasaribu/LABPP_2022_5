from abc import ABC, abstractmethod

class Contoh(ABC):
    #abstract class
    @abstractmethod
    def bergerak(self, nama):
        pass

class Contoh1(Contoh): #inheritence
    def bergerak(self, nama):
        self.__nama = nama #encapsulation
        print(f"{self.__nama} Berlari")

class Contoh2(Contoh): #inheritence
    def bergerak(self, nama):
        self.__nama = nama #encapsulation
        print(f"{self.__nama} Berjalan")

#polymorphism
budi = Contoh1()
siti = Contoh2()
budi.bergerak("Budi")
siti.bergerak("Siti")