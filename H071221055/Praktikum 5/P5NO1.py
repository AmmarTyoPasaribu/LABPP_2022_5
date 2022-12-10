# Program mengalikan dua buah matriks 2x2

a11 = int(input('Matriks A Baris 1 dan Kolom 1: '))
a12 = int(input('Matriks A Baris 1 dan Kolom 2: '))
a21 = int(input('Matriks A Baris 2 dan Kolom 1: '))
a22 = int(input('Matriks A Baris 2 dan Kolom 2: '))
b11 = int(input('Matriks B Baris 1 dan Kolom 1: '))
b12 = int(input('Matriks B Baris 1 dan Kolom 2: '))
b21 = int(input('Matriks B Baris 2 dan Kolom 1: '))
b22 = int(input('Matriks B Baris 2 dan Kolom 2: '))

# List untuk matriks 1 dan matriks 2
matriks = [[[a11, a12], [a21, a22]], [[b11, b12], [b21, b22]]] 

c11 = (matriks[0][0][0]*matriks[1][0][0]) + (matriks[0][0][1]*matriks[1][1][0])
c21 = (matriks[0][1][0]*matriks[1][0][0]) + (matriks[0][1][1]*matriks[1][1][0])

c12 = (matriks[0][0][0]*matriks[1][0][1]) + (matriks[0][0][1]*matriks[1][1][1])
c22 = (matriks[0][1][0]*matriks[1][0][1]) + (matriks[0][1][1]*matriks[1][1][1])

print(f'| {a11}, {a12} | x | {b11}, {b12} | = | {c11}, {c12} |')
print(f'| {a21}, {a22} |   | {b21}, {b22} |   | {c21}, {c22} |')
