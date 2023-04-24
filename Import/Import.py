import Funkcja


from enum import Enum
Menu = Enum('Menu', 'kwadrat prostokat kolo trojkat trapez')

wybor = int(input("""Jakie pole chcesz obliczyc:
1 - kwadrat
2 - protokat
3 - kolo
4 - trojkat
5 - trapez

"""))

if (wybor == Menu.kwadrat.value):
    a = int(input("Podaj dlugosc krawedzi: "))
    print("Pole wynosi: ", Funkcja.poleKwadratu(a))
elif(wybor == Menu.prostokat.value):
    a = int(input("Podaj dlugosc pierwszej krawedzi: "))
    b = int(input("Podaj dlugosc drugiej krawedzi: "))
    print("Pole wynosi: ", Funkcja.poleProstokąta(a,b))
elif(wybor == Menu.kolo.value):
    a = int(input("Podaj promien: "))
    print("Pole wynosi: ", Funkcja.poleKola(a))
elif(wybor == Menu.trojkat.value):
    a = int(input("Podaj dlugosc podstawy: "))
    h = int(input("Podaj dlugosc wysokosci: "))
    print("Pole wynosi: ", Funkcja.poleTrojkata(a,h))
elif(wybor == Menu.trapez.value):
    a = int(input("Podaj dlugosc pierwszej krawedzi: "))
    b = int(input("Podaj dlugosc drugiej krawedzi: "))
    h = int(input("Podaj dlugosc wysokosci: "))
    print("Pole wynosi: ", Funkcja.poleTrapezu(a,b,h))