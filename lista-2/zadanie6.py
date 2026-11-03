zadania = []
print("1. Dodaj zadanie")
print("2. Wyświetl zadania")
print("3. Usuń zadanie")
print("4. Wyświetl liczbę zadań")
print("0. Zakończ")
while True:
    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        zadanie = input("Podaj zadanie: ")
        zadania.append(zadanie)
        print("Zadanie dodane.")
    elif wybor == "2":
        if len(zadania) == 0:
            print("Brak zadań do wyświetlenia.")
        else:
            print("Lista zadań:")
            for i, zadanie in enumerate(zadania, start=1):
                print(f"{i}. {zadanie}")
    elif wybor == "3":
        if len(zadania) == 0:
            print("Brak zadań do usunięcia.")
        else:
            print("Lista zadań:")
            for i, zadanie in enumerate(zadania, start=1):
                print(f"{i}. {zadanie}")
            indeks = int(input("Podaj numer zadania do usunięcia: ")) - 1
            if 0 <= indeks < len(zadania):
                usuniete_zadanie = zadania.pop(indeks)
                print(f"Zadanie '{usuniete_zadanie}' zostało usunięte.")
            else:
                print("Nieprawidłowy numer zadania.")
    elif wybor == "4":
        print("Liczba zadań:", len(zadania))
    elif wybor == "0":
        print("Do widzenia!")
        break