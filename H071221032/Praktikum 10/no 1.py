import re

class Profile:
    def __init__(self):
        self.name = ""
        self.email = ""
        self.password = ""
    
    def getDetail(self):
        if self.name == "":
            return "Data saat ini kosong"
        else:
            return f"Data anda adalah:\nNama: {self.name}\nEmail: {self.email}\nPassword: {self.password}"

    def changeName(self):
        if self.name == "":
            print("Data saat ini kosong")
        else:
            self.name = input("Masukkan nama baru: ")
            print("Nama berhasil diubah")

    def countData(self):
        filename_count = input("Masukkan nama file: ")
        try:
            with open(f"{filename_count}.txt", "r") as file:
                read = file.read()
                count = re.findall("Email        :", read)
            return f"Terdapat {len(count)} data pada file {filename_count}"
        except(FileNotFoundError):
            return f"Tidak terdapat file dengan nama {filename_count}"

    def saveData(self):
        if self.name == "":
            print("Data saat ini kosong")
        else:
            filename_save = input("Masukkan nama file: ")
            
            try:
                with open(f"{filename_save}.txt", "r") as f:
                    pass
            except(FileNotFoundError):
                with open(f"{filename_save}.txt", "w") as f:
                    f.write("+" + "="*100 + "\n|Data yang tersimpan\n" + "+" + "="*100 + "\n")

            with open(f"{filename_save}.txt", "a") as file:
                file.write(f"|Nama         : {self.name}\n|Email        : {self.email}\n|Password     : {self.password}\n")
                file.write("+" + "="*100 + "\n")

    def newData(self):
        self.name = input("Masukkan Nama: ")

        while True:
            self.email = input("Masukkan Email: ")
            pattern = "(([a-z])|([0-9]))+@student.unhas.ac.id"
            if re.search(pattern, self.email):
                break
            else:
                print("Email yang Anda Masukkan Salah")
                continue

        while True:
            self.password = input("Masukkan Password: ")
            
            if len(self.password) >= 8 and len(self.password) <= 20:
                if re.search("[A-Z]",self.password) and re.search("[a-z]",self.password) and re.search("[0-9]",self.password):
                    break
                else:
                    print("Password yang anda masukkan terlalu lemah, gunakan minimal 1 huruf kapital, huruf kecil, dan angka")
                    continue
            else:
                print("Password harus memiliki Panjang 8 - 20 karakter")
                continue

user = Profile()
while True:
    print("="*50)
    print("Selamat datang, silahkan pilih opsi berikut:")
    print("1. Detail anda\n2. Ubah nama\n3. Jumlah data pada file\n4. Save data pada file\n5. Buat data baru\n6. Keluar")
    x = int(input("\n>> "))
    print("="*50)

    if x == 1:
        print(user.getDetail())
    elif x == 2:
        user.changeName()
    elif x == 3:
        print(user.countData())
    elif x == 4:
        user.saveData()
    elif x == 5:
        user.newData()
    elif x == 6:
        print("Sampai Jumpa Lagi")
        break
    else:
        print("Pilihan tidak valid")