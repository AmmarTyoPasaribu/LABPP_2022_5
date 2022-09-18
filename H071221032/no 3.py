seller = input("Masukkan nama seller: ")
gaji = float(input("Masukkan gaji pokok seller: $"))
penjualan = float(input("Masukkan total penjualan oleh seller: $"))

total = (0.15 * penjualan) + gaji
total = "{:.2f}".format(total)

print("Total = $" + str(total))