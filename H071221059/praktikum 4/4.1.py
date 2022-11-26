y = list(map(int, input().split()))

def adnan():
    new = [] # integer
    for i in range(len(y)):
        new.append(str(min(y)))
        y.remove(min(y))
    print(" ".join(new))
adnan()

# list : remove
# stack : pop