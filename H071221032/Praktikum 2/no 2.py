from dataclasses import replace


print("---Kalkulator tarif listrik---", "\n")
#x = ["R1", "R2", "R3", "B2", "B3", "I3", "P1"]

golongan = input("Golongan = ").upper()
#if golongan not in x:
#    print("\n", "Data tidak valid")
#    exit()
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

if golongan == 'R1' and daya == 900:
    tarif = 1352
elif golongan == 'R1' and daya == 1300:
    tarif = 1444.7
elif golongan == 'R1' and daya == 2200:
    tarif = 1444.7
elif golongan == 'R2' and daya >= 3500 and daya <=5500:
    tarif = 1699.53
elif golongan == 'R3' and daya >= 6600:
    tarif = 1699.53
elif golongan == 'B2' and daya >= 6600 and daya <= 200000:
    tarif = 1444.7
elif golongan == 'B3' and daya > 200000:
    tarif = 1114.74
elif golongan == 'I3' and daya >= 200000:
    tarif = 1314.12
elif golongan == 'P1' and daya >= 6600 and daya <= 200000:
    tarif = 1523.28
else:
    print("\n Data tidak valid")
    exit()

total = pemakaian * tarif
total = f'{total:,}'
tot = ""

for i in total:
    if i == '.':
        i = ","
    elif i == ",":
        i = "."
    tot = tot + i

print("\nJumlah tagihan anda =", tot)