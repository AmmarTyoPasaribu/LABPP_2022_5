harga = int(input("Masukkan harga barang: "))
uang = int(input("Masukkan jumlah uang yang dibayarkan: "))

kembalian = uang - harga

seratus = limapuluh = duapuluh = sepuluh = limaribu = duaribu = seribu = 0

while kembalian >= 1000:
    if kembalian >= 100000:
        kembalian = kembalian - 100000
        seratus = seratus + 1
    elif kembalian >= 50000:
        kembalian = kembalian - 50000
        limapuluh = limapuluh + 1
    elif kembalian >= 20000:
        kembalian = kembalian - 20000
        duapuluh = duapuluh + 1
    elif kembalian >= 10000:
        kembalian = kembalian - 10000
        sepuluh = sepuluh + 1
    elif kembalian >= 5000:
        kembalian = kembalian - 5000
        limaribu = limaribu + 1
    elif kembalian >= 2000:
        kembalian = kembalian - 2000
        duaribu = duaribu + 1
    elif kembalian >= 1000:
        kembalian = kembalian - 1000
        seribu = seribu + 1

print(seratus, "uang Rp. 100.000")
print(limapuluh, "uang Rp. 50.000")
print(duapuluh, "uang Rp. 20.000")
print(sepuluh, "uang Rp. 10.000")
print(limaribu, "uang Rp. 5.000")
print(duaribu, "uang Rp. 2.000")
print(seribu, "uang Rp. 1.000")