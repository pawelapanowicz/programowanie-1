def dodawanie(a, b):
    return a + b


def odejmowanie(a, b):
    return a - b


def mnozenie(a, b):
    return a * b


def dzielenie(a, b):
    return a / b


def potegowanie(a, b):
    return a ** b


def srednia(liczby):
    return sum(liczby) / len(liczby)


def wyswietl_menu():
    print("========== KALKULATOR ==========")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnozenie")
    print("4. Dzielenie")
    print("5. Potegowanie")
    print("6. Srednia")
    print("0. Zakoncz")
    print("================================")


def main():
    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcje: ")
        if wybor in ["1", "2", "3", "4", "5"]:
            a = int(input("Podaj pierwsza liczbe: "))
            b = int(input("Podaj druga liczbe: "))
            if wybor == "1":
                print("Wynik:", dodawanie(a, b))
            elif wybor == "2":
                print("Wynik:", odejmowanie(a, b))
            elif wybor == "3":
                print("Wynik:", mnozenie(a, b))
            elif wybor == "4":
                if b == 0:
                    print("Nie mozna dzielic przez zero.")
                else:
                    print("Wynik:", dzielenie(a, b))
            else:
                print("Wynik:", potegowanie(a, b))
        elif wybor == "6":
            ile = int(input("Ile liczb chcesz podac? "))
            liczby = []
            for i in range(ile):
                liczby.append(int(input(f"Liczba {i+1}: ")))
            print("Srednia:", srednia(liczby))
        elif wybor == "0":
            print("Koniec")
            break
        else:
            print("Nieznana opcja.")


if __name__ == "__main__":
    main()