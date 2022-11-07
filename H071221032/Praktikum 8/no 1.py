class Person:
    def __init__(self, name: str, age: str, isMale: bool, hobby: str, address: str):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.hobby = hobby
        self.address = address
    
    def getProfile(self):
        print("~~~ Profile Anda ~~~")
        print(f"Nama: {self.getName()}")
        print(f"Umur: {self.getAge()}")
        print(f"Jenis Kelamin: {self.getGender()}")
        print(f"Hobi: {self.getHobby()}")
        print(f"Alamat: {self.getAddress()}")

    def intro(self):
        print(f"Hai!, nama saya {self.getName()}. Saya berumur {self.getAge()} tahun, terlahir sebagai {self.getGender().lower()} dan tinggal di {self.getAddress()}. Saya sangat suka {self.getHobby().lower()}, itu merupakan hobi saya.")

    def roastSelf(self, num):
        if num > 3:
            num = num%4
        if num == 0:
            print(f"Hahaha nama anda <{self.getName()}> jelek sekali!")
        elif num == 1:
            print(f"LOL, hari gini masih hobi {self.getHobby()}.")
        elif num == 2:
            print(f"{self.getAddress()} itu di luar bumi ya? Kok jauh sekali hahahaha.")
        elif num == 3:
            print(f"Umur {self.getAge()} tapi mukanya kayak kakek-kakek!") if self.isMale == True else print(f"Umur {self.getAge()} tapi mukanya kayak nenek-nenek!")

    def setAge(self, age: int):
        self.age = age
    def getAge(self):
        return self.age

    def setName(self, name: str):
        self.name = name
    def getName(self):
        return self.name

    def setGender(self, isMale: bool):
        self.isMale = isMale
    def getGender(self):
        if self.isMale == True:
            return "Laki-laki"
        else:
            return "Perempuan"
    
    def setHobby(self, hobby):
        self.hobby = hobby
    def getHobby(self):
        return self.hobby

    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address

name = input("Masukkan nama anda: ")
age = int(input("Masukkan umur anda: "))
gender = bool(int(input("Masukkan jenis kelamin anda (0 untuk perempuan dan 1 untuk laki-laki): ")))
hobby = input("Masukkan hobi anda: ")
address = input("Masukkan alamat anda: ")

person = Person(name, age, gender, hobby, address)

random = 0

while True:
    try:
        x = int(input("\nPilihlah pilihan berikut sesuai angka yang tertera:\n1. Ubah nama anda\n2. Ubah umur anda\n3. Ubah jenis kelamin anda\n4. Ubah hobi anda\n5. Ubah alamat anda\n6. Tampilkan profile anda\n7. Perkenalkan diri anda\n8. Roasting diri anda sendiri\n9. Keluar\n\n>> "))
    except:
        print("Hanya menerima inputan integer!")
        continue

    if x == 1:
        name = input("Masukkan nama anda: ")
        person.setName(name)
    elif x == 2:
        age = int(input("Masukkan umur anda: "))
        person.setAge(age)
    elif x == 3:
        gender = bool(int(input("Masukkan jenis kelamin anda (0 untuk perempuan dan 1 untuk laki-laki): ")))
        person.setGender(gender)
    elif x == 4:
        hobby = input("Masukkan hobi anda: ")
        person.setHobby(hobby)
    elif x == 5:
        address = input("Masukkan alamat anda: ")
        person.setAddress(address)
    elif x == 6:
        person.getProfile()
    elif x == 7:
        person.intro()
    elif x == 8:
        person.roastSelf(random)
        random += 1
    elif x == 9:
        break
    else:
        print("Pilihan tidak valid")
        continue