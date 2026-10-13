poczatek = input("podaj początek zakresu: ")
koniec = input("podaj koniec zakresu: ")
for i in range(int(poczatek), int(koniec) + 1):
    if i % 2 == 0:
        print(i, "parzysta")
    else:
        print(i, "nieparzysta")
print("liczba liczb parzystych:", len(range(int(poczatek), int(koniec) + 1, 2)))