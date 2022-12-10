def myDay(hari):
    tahun = 0
    bulan = 0

    if hari // 365 >= 1:
        tahun = hari // 365
        hari = hari % 365

    if hari // 30 >= 1:
        bulan = hari // 30
        hari = hari % 30

    print(tahun, "tahun")
    print(bulan, "bulan")
    print(hari, "hari")

x = int(input())
myDay(x)