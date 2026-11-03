
koszt_dostawy = 12
cena_produktu = input("Podaj cenę produktu: ")
liczba_sztuk = input("Podaj liczbę sztuk: ")
wartosc_produktu = float(cena_produktu) * int(liczba_sztuk)
print("Wartość produktów wynosi", wartosc_produktu, "zł")
if wartosc_produktu >= 100:
    print("Koszt dostawy wynosi 0 zł")
else:
    print("Koszt dostawy wynosi", koszt_dostawy, "zł")
if wartosc_produktu >= 100:
    print("Do zapłaty", wartosc_produktu, "zł")
else:
    print("Do zapłaty", wartosc_produktu + koszt_dostawy, "zł")
