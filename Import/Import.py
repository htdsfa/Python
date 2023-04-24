import Funkcja


form enum import Enum
Menu = Enum("Menu", "kwadrat prostokat kolo trojkat trapez")

wybor = input("""Jakie pole chcesz obliczyc:
1 - kwadrat
2 - protokat
3 - kolo
4 - trojkat
5 - trapez

""")

if (wybor == "1"):
    a = int(input("Podaj dlugosc krawedzi: "))
    print("Pole wynosi: ", Funkcja.poleKwadratu(a))
elif(wybor == "2"):
    a = int(input("Podaj dlugosc pierwszej krawedzi: "))
    b = int(input("Podaj dlugosc drugiej krawedzi: "))
    print("Pole wynosi: ", Funkcja.poleProstokąta(a,b))
elif(wybor == "3"):
    a = int(input("Podaj promien: "))
    print("Pole wynosi: ", Funkcja.poleKola(a))
elif(wybor == "4"):
    a = int(input("Podaj dlugosc podstawy: "))
    h = int(input("Podaj dlugosc wysokosci: "))
    print("Pole wynosi: ", Funkcja.poleTrojkata(a,h))
elif(wybor == "5"):
    a = int(input("Podaj dlugosc pierwszej krawedzi: "))
    b = int(input("Podaj dlugosc drugiej krawedzi: "))
    h = int(input("Podaj dlugosc wysokosci: "))
    print("Pole wynosi: ", Funkcja.poleTrapezu(a,b,h))