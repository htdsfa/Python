def sumaLiczb(liczba):
    suma = 0
    for liczba in range (1,liczba+1):
        suma = suma + liczba
    return suma

def sumaLiczb2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)])
def sumaLiczb3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)})
def sumaLiczb4(liczba):
    return sum((liczba for liczba in range(1,liczba+1)))
def sumaLiczb5(liczba):
    return (1 + liczba)/2*liczba


print(sumaLiczb(5))
print(sumaLiczb2(5))
print(sumaLiczb3(5))
print(sumaLiczb4(5))
print(sumaLiczb5(5))