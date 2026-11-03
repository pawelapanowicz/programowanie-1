kontakty = {}
while True:
    print("========== KSIAZKA KONTAKTOW ==========")
    print("1. Dodaj kontakt")
    print("2. Wyswietl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Edytuj kontakt")
    print("5. Usun kontakt")
    print("0. Zakoncz")
    print("=======================================")
    wybor = input("Wybierz opcje: ")
    if wybor == "1":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        telefon = input("Telefon: ")
        if telefon in kontakty:
            print("Taki numer już istnieje.")
        else:
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt dodany.")
    elif wybor == "2":
        if len(kontakty) == 0:
            print("Brak kontaktów.")
        for telefon in kontakty:
            imie, nazwisko = kontakty[telefon]
            print("Telefon:", telefon, "Imie:", imie, "Nazwisko:", nazwisko)
    elif wybor == "3":
        telefon = input("Telefon: ")
        if telefon in kontakty:
            imie, nazwisko = kontakty[telefon]
            print("Imie:", imie, "Nazwisko:", nazwisko)
        else:
            print("Nie ma takiego numeru.")
    elif wybor == "4":
        telefon = input("Telefon: ")
        if telefon in kontakty:
            imie = input("Nowe imie: ")
            nazwisko = input("Nowe nazwisko: ")
            kontakty[telefon] = [imie, nazwisko]
            print("Kontakt zmieniony.")
        else:
            print("Nie ma takiego numeru.")
    elif wybor == "5":
        telefon = input("Telefon: ")
        if telefon in kontakty:
            del kontakty[telefon]
            print("Kontakt usunięty.")
        else:
            print("Nie ma takiego numeru.")
    elif wybor == "0":
        print("Koniec")
        break
