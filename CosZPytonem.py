cenaNetto = 2300
VAT = 23
obliczonyVAT = (1+VAT/100)
cenaBrutto = cenaNetto * obliczonyVAT
print(cenaBrutto)

----------------------------------------

x = 1; y = 2; z = 3;

a,b,c = 1 , "cos" , False

a = b = c = 1

----------------------------------------

abs(-2) #daje 2
import nazwaBiblioteki #importuje biblioteke
nazwaBiblioteki.funkcja #uzycie funckji 
from nazwaBiblioteki import funkcja #nie trzeba pisac nazwaBiblioteki.funkcja
from nazwaBiblioteki import * #importuje wszystkie funkcje z biblioteki
help(funkcja) #pokazuje co robi dana funkcja

----------------------------------------

a = input() #zapisuje dane jako ciąg znaków
int(a) #zamienia zmienną na liczbe
float(a) #zamienia zmienną na liczbe

a = int(input("Podaj pierwszą liczbę: ")) #zamienia zmienna odrazu na liczbe
b = int(input("Podaj pierwszą liczbę: ")) #zamienia zmienna odrazu na liczbe

print("Wynki dodawania to:" + str(a+b)) #pokaze: Wynki dodawania to: np 15
print("Wynki dodawania to:", a+b) #pokaze: Wynki dodawania to: np 15
print("Wynki dodawania",a,"+",b, "to:", a+b) #pokaze: Wynki dodawania 5 + 10 to: np 15

----------------------------------------

wybor = input("* - mnożenie, / - dzielenie, + - dodawanie, - - odejmowanie")

a = int(input("Pierwsza liczba"))
b = int(input("Druga liczba"))

if (wybor == "*"):
    print(a * b)
elif (wybor == "/"):
    if(b == 0):
        print("Nie dziel przez 0")
    else:
        print(a / b)
elif (wybor == "+"):
    print(a + b)
elif (wybor == "-"):
    print(a - b)
else:
    print("Nie wybrano nic")

----------------------------------------

liczba = 0

while liczba <= 5:
    liczba += 1
    print(liczba)

----------------------------------------

wynik = 0

i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1
print("Wynik: ",wynik)

----------------------------------------

wynik = 0

i = 0
while i < 4:
    x = int(input("Podaj liczbę: "))
    wynik += x
    i += 1
print("Wynik: ",wynik)

----------------------------------------

for i in range(0,4):
    x = int(input("Podaj liczbe: "))
    wynik += x
print("Wynik: ",wynik)

----------------------------------------

wynik = 0
i = 0

while i<3:
    x=int(input("Podaj dodatnią liczbę: "))
    if(x>0):
        wynik +=x
    else:
        print("Liczba nie dodatnia")
        break #przerywa petlę a contiune ją kontynuje
    print("aktualny wynik: ",wynik)
    i+=1

----------------------------------------

