x = input("Masukkan nama file: ")
nama_filex = x + ".txt"

y = input("Masukkan nama file baru (copy): ")
nama_filey = y + ".txt"

try:
    def salin(nama_filex, nama_filey):
        with open(nama_filex) as old:
            file_asli = old.read()
            with open(nama_filey, "w") as new:
                new.write(file_asli)
                print("Berhasil")
    salin(nama_filex, nama_filey)
except:
    print("gagal")