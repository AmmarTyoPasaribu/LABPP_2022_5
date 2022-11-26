number = int(input())

def faktorial(number):
    if number > 1:
        return number*faktorial(number-1)
    return 1
print(f"{faktorial(number)}")