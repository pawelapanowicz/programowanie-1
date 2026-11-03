warsztat_python = set()
warsztat_ai = set()
while True:
    print("1. Zapisz na Python")
    print("2. Zapisz na AI")
    print("3. Wyswietl uczestnikow")
    print("4. Uczestnicy obu warsztatow")
    print("5. Wszyscy unikalni uczestnicy")
    print("0. Zakoncz")
    wybor = input("Wybierz opcje: ")
    if wybor == "1" or wybor == "2":
        imie = input("Imie: ")
        nazwisko = input("Nazwisko: ")
        uczestnik = (imie, nazwisko)
        if wybor == "1":
            if uczestnik in warsztat_python:
                print("Ta osoba jest juz zapisana.")
            else:
                warsztat_python.add(uczestnik)
                print("Dodano uczestnika.")
        else:
            if uczestnik in warsztat_ai:
                print("Ta osoba jest juz zapisana.")
            else:
                warsztat_ai.add(uczestnik)
                print("Dodano uczestnika.")
    elif wybor == "3":
        print("Python:")
        for imie, nazwisko in sorted(warsztat_python):
            print(imie, nazwisko)
        print("AI:")
        for imie, nazwisko in sorted(warsztat_ai):
            print(imie, nazwisko)
    elif wybor == "4":
        wspolni = warsztat_python & warsztat_ai
        print("Uczestnicy obu warsztatow:")
        for imie, nazwisko in sorted(wspolni):
            print(imie, nazwisko)
    elif wybor == "5":
        wszyscy = warsztat_python | warsztat_ai
        print("Wszyscy unikalni uczestnicy:")
        for imie, nazwisko in sorted(wszyscy):
            print(imie, nazwisko)
    elif wybor == "0":
        print("Koniec")
        break
    else:
        print("Nieznana opcja.")