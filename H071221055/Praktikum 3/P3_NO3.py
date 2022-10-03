total = int(input('Total :'))
tunai = int(input('Uang Tunai :'))
kembalian = tunai - total
uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

if total < tunai:
    for x in uang:
        bagi = kembalian // x
        print('%d uang Rp %d' % (bagi, x))
        kembalian -= bagi * x
elif total > tunai:
    print('TIDAK MENERIMA KASBON')
else:
    print('Terima Kasih,Selamat Datang Kembali')

# x = x+1
# x += 1