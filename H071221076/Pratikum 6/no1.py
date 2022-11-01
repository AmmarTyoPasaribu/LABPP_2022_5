nama_file = input()
file_copy = input()
try:
    with open (nama_file+'.txt', 'r') as file :
        print(file.read())
        nama_file = file.read()
        isi = file.read()

        with open (file_copy+'.txt', 'w') as file1 :
            file1.write(isi)

    print ('Berhasil')

except :
    print ('Gagal')