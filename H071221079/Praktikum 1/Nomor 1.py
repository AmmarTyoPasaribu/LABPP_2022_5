import math  #import math biar bisa pake yg dri pythonnya ngab kek pi akar sincostan dkk
print('H = KETINGGIAN MENARA')
print('A = SUDUT ELEVASI PENGAMAT TERHADAP UJUNG BELAKANG KAPAL')
print('B = SUDUT ELEVASI PENGAMAT TERHADAP UJUNG DEPAN KAPAL')

h = float(input('Masukkan nilai H : '))
a = float(input('Masukkan nilai A : '))
b = float(input('Masukkan nilai B : '))

x = math.tan(math.radians(a))*h   # a di radiantkan terus di tan kan
                                  
y = math.tan(math.radians(b))*h   # b di radiantkan terus di tan kan

panjang_kapal = round(math.sqrt(x-y)**2,1)   # math sqrt untuk akar ngab

print(panjang_kapal,'m')