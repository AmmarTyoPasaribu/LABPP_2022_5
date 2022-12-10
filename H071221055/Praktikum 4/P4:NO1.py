def urutan():
    n = int(input("banyak array: "))
    list = []
    for i in range(0, n):
        element = int(input("- "))
        list.append(element)

    print("sebelum diurut: ", list)

    for i in range(0, n):
        for j in range(0, n):
            if list[i] < list[j]:
                temp = list[i]              #bubble sort line 10-15
                list[i] = list[j]
                list[j] = temp

    print("setelah diurut: ", list)

urutan()
