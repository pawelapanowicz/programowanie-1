liczba_punktow = input("Podaj liczbę punktów: ")
if int(liczba_punktow) > 100:
    print("Błędne dane")
else:
    if int(liczba_punktow) >= 90:
        print("liczba_punktow:", liczba_punktow), print("Uzyskana Ocena: 5.0")
    elif int(liczba_punktow) >= 80:
        print("liczba punktów:", liczba_punktow), print("Uzyskana Ocena: 4.5")
    elif int(liczba_punktow) >= 70:
        print("liczba punktów:",  liczba_punktow), print("Uzyskana Ocena: 4.0")
    elif int(liczba_punktow) >= 60:
        print("liczba punktów:", liczba_punktow), print("Uzyskana Ocena: 3.5")
    elif int(liczba_punktow) >= 50:
        print("liczba punktów:", liczba_punktow), print("Uzyskana Ocena: 3.0")
    else:
        print("liczba punktów:", liczba_punktow), print("Uzyskana Ocena: 2.0")