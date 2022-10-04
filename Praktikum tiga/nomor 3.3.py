a = int(input())
b = int(input())

kembalian = b-a

seratus = limapuluh = duapuluh = sepuluh = lima = dua = satu = 0 # jumlah lembar

while(kembalian >= 1_000):
    print(kembalian)
    if kembalian >= 100_000:
        seratus += 1
        kembalian -= 100_000
    elif kembalian >= 50_000:
        limapuluh += 1
        kembalian -= 50_000
    elif kembalian >= 20_000:
        duapuluh += 1
        kembalian -= 20_000
    elif kembalian >= 10_000:
        sepuluh += 1
        kembalian -= 10_000
    elif kembalian >=5_000:
        lima += 1
        kembalian -= 5_000
    elif kembalian >= 2_000:
        dua += 1
        kembalian -= 2_000
    elif kembalian >= 1_000:
        satu += 1
        kembalian -= 1_000
print("%d uang Rp. 100.000" % seratus)
print("%d uang Rp. 50.000" % limapuluh)
print("%d uang Rp. 20.000" % duapuluh)
print("%d uang Rp. 10.000" % sepuluh)
print("%d uang Rp. 5.000" % lima)
print("%d uang Rp. 2.000" % dua)
print("%d uang Rp. 1.000" % satu)

    
    
    



