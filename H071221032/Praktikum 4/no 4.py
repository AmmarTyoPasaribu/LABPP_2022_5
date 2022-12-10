x = y = 0
    
def robot():
    global x, y, move
    
    for i in move:
        if i == "R":
            x += 1
            print(x, y)
        elif i == "L":
            x -= 1
            print(x, y)
        elif i == "U":
            y += 1
            print(x, y)
        elif i == "D":
            y -= 1
            print(x, y)

move = input()
print(x, y)
robot()

while True:
    move = input()

    if move.lower() == "end":
        break
    
    robot()