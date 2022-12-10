try:
    x = input() + ".txt"
    file1 = open(x,"r")

    y = input() + ".txt"

    file2 = open(y, "w")

    for i in file1:
        if i[len(i)-1] == "\n":
            space = " "*(18-len(i))
        else:
            space = " "*(17-len(i))

        file2.write(space + i)

    print("Berhasil")
except:
    print("Gagal")

file1.close()
file2.close()