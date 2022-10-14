def myDay(h):
    tahun = h//360
    sisahari = h%360
    bulan = sisahari//30
    hari = sisahari % 30
    print(f"{tahun} tahun")
    print(f"{bulan} bulan")
    print(f"{hari} hari")

a = int(input())
print()
print(myDay(a))