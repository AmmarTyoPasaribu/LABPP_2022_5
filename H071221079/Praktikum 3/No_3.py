a = int(input('a: '))#harga barang
b = int(input('b: '))#jumlah uang
kembalian = b - a #40000
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if a < b: #ya
    for i in uang:
        c = kembalian // i #40000 //20000
        print('%d uang Rp. %d '% (c, i))
        kembalian = kembalian - c * i
elif a == b:
    print('0')
else:
    print('Inputan b harus lebih besar dari pada a')