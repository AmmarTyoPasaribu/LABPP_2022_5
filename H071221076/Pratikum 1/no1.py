import math
#panjang kapal = akar

h= float(input("masukkan tinggi menara: "))
a= float(input("masukkan sudut terhadap ujunng depan kapal: "))
b= float(input("masukkan sudut terhadap ujung belakang kapal: "))

x = math.tan(math.radians(a))*h
y = math.tan(math.radians(b))*h

panjang_kapal = math.sqrt((x-y)**2)
z= round(panjang_kapal, 1)

print(z , "m")