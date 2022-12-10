p = 0
q = 1
n = int(input("Masukkan n: "))
x = 2
List = [p, q]

while x < n:
  fibonacci = p + q
  List += [fibonacci]
  p = q
  q = fibonacci
  x += 1

output = ""

for i in List:
    output += str(i) + " "

print(output)