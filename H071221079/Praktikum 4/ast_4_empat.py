from types import NoneType


nilai = int(input())
def nilai_f(nilai):
    if nilai > 1:
        return nilai*nilai_f(nilai-1)
    elif nilai < 0:
        return NoneType
    return 1
print(nilai_f(nilai))