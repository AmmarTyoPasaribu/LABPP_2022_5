def ast1():
    n = int(input("Banyak Element Array : "))
    datalist = []
    for i in range(0,n):
        element = int(input("- "))
        datalist.append(element)

    print("Sebelum diurut : ",datalist)
    
    for i in range(0,n):
        for j in range(0,n):
            if datalist[i]<datalist[j]:
                iniv = datalist[i]
                datalist[i] = datalist[j]
                datalist[j] = iniv

    print("Setelah diurut : ",datalist)

ast1()