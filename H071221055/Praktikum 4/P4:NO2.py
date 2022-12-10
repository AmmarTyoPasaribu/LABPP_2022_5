def IsPrime():
    n = int(input('Bilangan bulat : '))
    if n == 2 or n == 3: #dikhususkan
        print('ini bilangan prima')
    elif n == 1 or n % 2 == 0 or n % 3 == 0:
        print('ini bukan bilangan prima')
    else :
        print('ini bilangan prima')
IsPrime()