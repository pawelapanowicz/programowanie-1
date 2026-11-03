ksiazki = []
while True:
    print("========== BIBLIOTEKA ==========")
    print("1. Dodaj ksiazke")
    print("2. Wyswietl wszystkie ksiazki")
    print("3. Wypozycz ksiazke")
    print("4. Zwroc ksiazke")
    print("5. Usun ksiazke")
    print("0. Zakoncz")
    print("===============================")
    wybor = input("Wybierz opcje: ")
    if wybor == "1":
        tytul = input("Tytul: ")
        autor = input("Autor: ")
        ksiazki.append({"tytul": tytul, "autor": autor, "status": "dostepna"})
        print("Ksiazka dodana.")
    elif wybor == "2":
        if len(ksiazki) == 0:
            print("Katalog jest pusty.")
        for i in range(len(ksiazki)):
            print(i + 1, ksiazki[i]["tytul"], ksiazki[i]["autor"], ksiazki[i]["status"])
    elif wybor == "3":
        numer = int(input("Numer ksiazki: ")) - 1
        if numer < 0 or numer >= len(ksiazki):
            print("Nieprawidlowy numer.")
        elif ksiazki[numer]["status"] == "wypozyczona":
            print("Ksiazka jest juz wypozyczona.")
        else:
            ksiazki[numer]["status"] = "wypozyczona"
            print("Wypozyczono:", ksiazki[numer]["tytul"])
    elif wybor == "4":
        numer = int(input("Numer ksiazki: ")) - 1
        if numer < 0 or numer >= len(ksiazki):
            print("Nieprawidlowy numer.")
        elif ksiazki[numer]["status"] == "dostepna":
            print("Ksiazka nie jest wypozyczona.")
        else:
            ksiazki[numer]["status"] = "dostepna"
            print("Zwrocono:", ksiazki[numer]["tytul"])
    elif wybor == "5":
        numer = int(input("Numer ksiazki: ")) - 1
        if numer < 0 or numer >= len(ksiazki):
            print("Nieprawidlowy numer.")
        else:
            print("Usunieto:", ksiazki[numer]["tytul"])
            del ksiazki[numer]
    elif wybor == "0":
        print("Koniec")
        break
    else:
        print("Nieznana opcja.")
