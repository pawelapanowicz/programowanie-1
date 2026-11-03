cena_wody = []
cena_soku = []
cena_coli = []
zakoncz = []
print("Wybierz napój:")
print("1. Woda - 3 zł")
print("2. Sok - 5 zł")
print("3. Cola - 6 zł")
print("0. Zakoncz")
while True:
    wybor = input("Wybierz produkty:")
    koszyk = 0
    if wybor == "1":
        print("Wybrano: Woda, cena: 3 zł")
        cena_wody.append(3)
        koszyk += 3
    elif wybor == "2":
        print("Wybrano: Sok, cena: 5 zł")
        cena_soku.append(5)
        koszyk += 5
    elif wybor == "3":
        print("Wybrano: Cola, cena: 6 zł")
        cena_coli.append(6)
        koszyk += 6
    elif wybor == "0":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")
suma = sum(cena_wody) + sum(cena_soku) + sum(cena_coli)
print("Łącznie do zapłaty:", suma, "zł")
