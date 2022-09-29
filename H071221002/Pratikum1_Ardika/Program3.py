import math
jari_jari_alas = int(input('Masukkan Jari-jari : '))
tinggi = int(input('Masukkan Tinggi : '))

r=jari_jari_alas
t=tinggi

phi = math.pi
s = (r*r)+(t*t)
S = s**0.5

volume = (phi*r*r*t)/3
luas_permukaan = (phi*r*S)+phi*r*r

print('Volume : ', round(volume,2))
print('Luas Permukaan : ', 
round(luas_permukaan,2))