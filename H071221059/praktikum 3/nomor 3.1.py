num = int(input(' '))
num1 = int(input(' '))

if num < num1:
    for i in range(1, num1+1):
        print(i , end = '\n' if num % num1 == 0 else ' ')
