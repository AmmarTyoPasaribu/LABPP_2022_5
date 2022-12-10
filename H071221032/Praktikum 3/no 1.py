x = int(input("Masukkan nilai X: "))
y = int(input("Masukkan nilai Y: "))

print("\n-----------------")

horizontal = x
output = ""

for i in range(1, y + 1):
    output += str(i) + " "
    horizontal = horizontal - 1
    
    if horizontal == 0 or i == y:
        print(output)
        output = ""
        horizontal = x