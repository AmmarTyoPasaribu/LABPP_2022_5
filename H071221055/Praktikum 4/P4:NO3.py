n = int(input('Masukkan angka:'))
def nilai_faktorial(n):
    if n > 1:
        return n*nilai_faktorial(n-1)
    elif n < 0:
        return 'none'
    else:
        return 1
print(nilai_faktorial(n))
