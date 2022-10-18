
def rot_str (kata):
    N_temp = kata + kata
    N_size = len (kata)         #len untuk membaca berapa panjang dalam inputan

    for i in range (N_size):
        for ii in range (N_size):
            print(N_temp[i+ii+1], end="")

        print(end="|")

kata = str (input('Masukkan Kata :'))
rot_str(kata)