x = input("Masukkan nama file: ") + ".txt"
y = input("Masukkan nama file baru (copy): ") + ".txt"

try:
    with open(x, "r") as old:
        file_asli = old.readlines()
        nilai = []
        for x in file_asli:
            nilai.append(len(x))
            with open(y, "w") as new:
                for i in file_asli:
                    new.write(i.rjust(max(nilai)))
    print("Berhasil")
except:
    print("Gagal")
