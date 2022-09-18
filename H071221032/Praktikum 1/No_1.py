import math
from re import A

h = int(input('h: '))
a = int(input('a: '))

rad = math.radians(a)
x =math.tan(rad)

b = int(input('b: '))
rad1 = math.radians(b)
y =math.tan(rad1)

hasil = round(h * x - h * y,1)
print(hasil,'m')

