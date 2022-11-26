list = input()

def all_string_rotation (y):
    banyak = len (y)
    for i in range (1,banyak+1):
        rotasi = list[banyak-i:] + list[:banyak-i]
        if banyak == 1:
            print (rotasi)
        else: 
            print (rotasi,end=' | ')

all_string_rotation(list)
