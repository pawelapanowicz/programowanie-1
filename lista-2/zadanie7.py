magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}
print("1. Stan magazynu")
print("2. Przyjęcie towaru")
print("3. Wydanie towaru")
print("0. Zakończ")
while True:
    wybor = input("Wybierz opcję: ")
    if wybor == "1":
        print("Stan magazynu:")
        for produkt, ilosc in magazyn.items():
            print(f"{produkt}: {ilosc} szt.")
    elif wybor == "2":
        produkt = input("Nazwa produktu: ")
        ilosc = int(input("Liczba sztuk: "))
        if produkt in magazyn:
            magazyn[produkt] += ilosc
        else:
            magazyn[produkt] = ilosc
        print(f"Zaktualizowano stan produktu.")
    elif wybor == "3":
        produkt = input("Nazwa produktu do wydania: ")
        ilosc = int(input("Liczba sztuk: "))
        if produkt in magazyn and magazyn[produkt] >= ilosc:
            magazyn[produkt] -= ilosc
            print(f"Wydano {ilosc} szt. produktu '{produkt}'.")
        else:
            print(f"Nie można wydać {ilosc} szt. produktu '{produkt}'. Brak wystarczającej ilości.")
    elif wybor == "0":
        print("Do widzenia!")
        break