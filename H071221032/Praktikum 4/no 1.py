def faktorial():
    global x, a

    while True:
        x = x * a
        a -= 1
        
        if a < 2:
            break
        
    print(x)
    
x = int(input())
a = x - 1

if x > 1:
    faktorial()
else:
    x = 1
    print(x)