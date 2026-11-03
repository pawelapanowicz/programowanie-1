haslo = "Python123"
proby = 3
while proby > 0:
    wpisane_haslo = input("Podaj hasło: ")
    if wpisane_haslo == haslo:
        print("Logowanie udane!")
        break
    else:
        proby -= 1
        print("Nieprawidłowe hasło. Pozostałe próby:", proby)
if proby == 0:
    print("Przekroczono liczbę prób. Konto zablokowane.")