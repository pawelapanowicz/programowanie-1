while True:
    print("========== KALKULATOR ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia z podanych liczb")
    print("0. Zakoncz")
    print("================================")
    wybor = input("Wybierz opcje: ")
    if wybor in ["1", "2", "3", "4", "5"]:
        a = float(input("Pierwsza liczba: "))
        b = float(input("Druga liczba: "))
        if wybor == "1":
            print("Wynik:", a, "+", b, "=", a + b)
        elif wybor == "2":
            print("Wynik:", a, "-", b, "=", a - b)
        elif wybor == "3":
            print("Wynik:", a, "*", b, "=", a * b)
        elif wybor == "4":
            if b == 0:
                print("Nie można dzielić przez zero.")
            else:
                print("Wynik:", a, "/", b, "=", a / b)
        else:
            print("Wynik:", a, "^", b, "=", a ** b)
    elif wybor == "6":
        ile = int(input("Ile liczb? "))
        if ile <= 0:
            print("Liczba elementów musi być dodatnia.")
        else:
            suma = 0
            for i in range(ile):
                suma += float(input(f"Liczba {i+1}: "))
            print("Srednia:", suma / ile)
    elif wybor == "0":
        print("Koniec")
        break
    else:
        print("Nieznana opcja.")
