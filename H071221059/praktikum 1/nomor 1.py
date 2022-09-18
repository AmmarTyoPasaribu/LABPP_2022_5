import math

# panjang kapal = akar

h = float(input('Masukkan tinggi kapal '))
a = float(input('Masukkan sudut terhadap ujung depan kapal '))
b = float(input('Masukkan sudut terhadap ujung belakang kapal '))

x = math.tan(math.radians(a)) * h
y = math.tan(math.radians(b)) * h

panjang_kapal = math.sqrt((x-y)**2)
z = round(panjang_kapal, 1)

print(z)