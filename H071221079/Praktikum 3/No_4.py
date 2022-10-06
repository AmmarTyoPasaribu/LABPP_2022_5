a = int(input('masukkan jumlah baris= '))
for i in range(1, a+1):
    print((a-i) * ' ' + (i * '* ') + ((i-1) * '* '))