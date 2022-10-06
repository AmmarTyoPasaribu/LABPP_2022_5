a = int(input('Masukkan data: '))
b = int(input('Masukkan data: '))

if a < b:
    for i in range(1, b+1):
        print(i , end = ' \n' if i % a == 0 else ' ')
else:
    print('Invalid')


