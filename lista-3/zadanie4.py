opisy = []
kwoty = []
while True:
    print("========= MOJ BUDZET =========")
    print("1. Dodaj przychod")
    print("2. Dodaj wydatek")
    print("3. Wyswietl historie operacji")
    print("4. Wyswietl stan konta")
    print("5. Podsumowanie finansowe")
    print("7. Usun operacje")
    print("0. Zakoncz")
    print("==============================")
    wybor = input("Wybierz opcje: ")
    if wybor == "1":
        opis = input("Opis: ")
        kwota = float(input("Kwota: "))
        if kwota <= 0:
            print("Kwota musi byc dodatnia.")
        else:
            opisy.append(opis)
            kwoty.append(kwota)
            print("Dodano przychod.")
    elif wybor == "2":
        opis = input("Opis: ")
        kwota = float(input("Kwota: "))
        if kwota <= 0:
            print("Kwota musi byc dodatnia.")
        else:
            opisy.append(opis)
            kwoty.append(-kwota)
            print("Dodano wydatek.")
    elif wybor == "3":
        if len(opisy) == 0:
            print("Historia jest pusta.")
        for i in range(len(opisy)):
            print(i + 1, opisy[i], kwoty[i], "zl")
    elif wybor == "4":
        print("Stan konta:", sum(kwoty), "zl")
    elif wybor == "5":
        przychody = sum(k for k in kwoty if k > 0)
        wydatki = -sum(k for k in kwoty if k < 0)
        print("Suma przychodow:", przychody, "zl")
        print("Suma wydatkow:", wydatki, "zl")
        print("Bilans:", sum(kwoty), "zl")
        if wydatki == 0:
            print("Brak wydatkow.")
        else:
            print("Najwiekszy wydatek:", -min(kwoty), "zl")
    elif wybor == "7":
        numer = int(input("Numer operacji: ")) - 1
        if 0 <= numer < len(opisy):
            print("Usunieto:", opisy[numer])
            del opisy[numer]
            del kwoty[numer]
        else:
            print("Nieprawidlowy numer.")
    elif wybor == "0":
        print("Koniec")
        break
    else:
        print("Nieznana opcja.")
