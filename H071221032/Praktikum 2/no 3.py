angka = input("Input 5 bilangan bulat dipisahkan oleh spasi: ").split()
try:
    angka = [int(int_angka) for int_angka in angka]
except(ValueError):
    print("\nInputan tidak valid")
    exit()

ganjil = 0
genap = 0
negatif = 0
positif = 0

for i in angka:
    if i%2 == 0:
        genap = genap + 1
    else:
        ganjil = ganjil + 1
    
    if i > 0:
        positif = positif + 1
    elif i < 0:
        negatif = negatif + 1

print(genap, "Angka Genap")
print(ganjil, "Angka Ganjil")
print(positif, "Angka Positif")
print(negatif, "Angka Negatif")