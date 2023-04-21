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

for i in range(0,4): #od 0 do 4
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

#lista[]
lista = ["cos"]
lista[0] = "inne"
print("cos" in lista) #wypisze true jesli znajduje się w liscie lub false not in działa tak samo
print([4] + lista) #dodaje na poczatek listy 4

print(len(lista)) #pokazuje ilość elementów w liscie
lista.append(4) #dodaje na koniec listy i zmienia ją
lista.extend([4,5,6,7]) #powieksza liste
lista.insert(1, "csotam") #dodaje element na dany indeks
lista.index("cos") #pokaże nam na jakiej pozycji znajdzuje sie dany element
lista.sort() #sortuje rosnąco liste
lista.sort(reverse=True) #sortuje malejąco liste
lista.max() #pokaże najwiekszą wartość
lista.min() #pokazę najmniejszą wartość
lista.count(1) #pokaże ile jest danych elementów w liscie
lista.pop() #usuwa ostatni element
lista.remove() #usuwa pierwszy napotkany element
lista.clear() #czysci listę
lista.reverse() #zmienia kolejność listy

----------------------------------------

#krotka () albo bez
#nie można jej zmieniac
#używac wtedy jak jestes pewny ze nie bedziesz nic dodawał
krotka = 1, 2, 3, 4, 5 #bez nawiasów lub zwykłe()

----------------------------------------

#dictionary{}
słownik = {49: "jakies slowo", 50: "kolejne słowo"}
słownik[49] #pobranie wartosci
słownik[51]= "cos tam"          }dodaje nowa wartosc
słownik.update({52: "takk"})    }dodaje nowa wartosc

----------------------------------------

#zbiory{}
#nie pokazuje tych samych elementów i od razu ją sortuje rosnaco
a={1, 4,30,-5,4}
a.add(4) #dodaje element
set(a) #zamiena liste na zbiór

print(a%b) #pokazuje wspólne elementy zbiorów
print(a|b) #pokazuje wszytkie elementy zbiorów nie sortuje nie pokazuje dwa razy tych samych elementów
print(a-b) #pokazuje zbiór a bez b
print(a^b) #wyklucza wspólne wartosci
a.discard(1) #usuwa podany element
a.issubset(b) #sprawdzanie czy a jest pod zbiorem b czyli czy ma takie same wartosci
print("\n") #daje podwójny enter

----------------------------------------

for name, age, sex in lista #wypisanie wartości z listy za pomoca pętli
for key in dictionary:
    print(key, dictionary[key]) #wypisane wartości ze słwonika za pomoca pętli
dictionary.items() #zamiena słownik na liste i krotki

----------------------------------------

#transformacja listy
liczby = [1,3,4,5,7]
potegiDwójki = [element ** 2 for element in liczby]
liczbyParzyste = [element for element in liczby if (element % 2 == 0)]

----------------------------------------

#generator
evenNumbers = (element for element in range (400) if (element % 2 == 0)) #generator
for item in evenNumbers: #wypisanie elementów z generatora
    print(item)

----------------------------------------

#wyrażenie słownikowe
namesLength = { klucz : wartosc for slownik in slowniki}

----------------------------------------

#funkcja
def nazwa_funkcji(parametr):
    print("Witaj",parametr,"co u ciebie?")

nazwa_funkcji(Wojtku)

def nazwa_funkcji_2(parametr1,parametr2):
    cos cosocos
    return parametr1+parametr2
print(5 * nazwa_funkcji_2())