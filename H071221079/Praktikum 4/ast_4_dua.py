def isiFPB(a,b): #20,30 ->30,10 ->10,0
    if (b==0):
        return a
    else:
        return isiFPB(b,a%b) #30, 20 % 30 = 10 -> 10,30 % 10= 0

input_a = int(input())
input_b = int(input())

print('FPB( %s,%s)='%(input_a,input_b),isiFPB(input_a,input_b))

if input_a == 0 or input_b == 0:
    print('salahhhh')







