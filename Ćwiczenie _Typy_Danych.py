defi={}

while (True):
    print("1 - Dodaj definicję", "2 - Znajdź definicję", "3 - Usuń definicję", "4 - Zakończ")
    wybor = int(input("Wybierz co chcesz robic "))
    if (wybor == 1):
        klucz = input("Podaj klucz ")
        if klucz in defi:
            print("Klucz o takiej nazawie juz istnieje")
        else:
            definicja = input("Podaj definicję ")
            defi[klucz] = definicja
            print("Dodano")
            print(defi)
    elif (wybor == 2):
        klucz = input("Co chcesz znaleźć? ")
        if klucz in defi:
            print(defi[klucz])
        else:
            print("Nie ma takiej")
    elif (wybor == 3):
        usun = input("Podaj definicję do usunięcia ")
        if usun in defi:
            del(defi[usun])
    else:
        break