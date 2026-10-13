temperatura = input("Podaj temperaturę: ")
ludzie = input("Czy ktoś jest w domu?: ")
okno = input("Czy okno jest otwarte?: ")
if okno.lower() == "tak":
    print("Ogrzewanie: WYŁĄCZONE"), print("Powód: okno jest otwarte")
else:
    if ludzie.lower() == "tak":
        if float(temperatura) < 20:
            print("Ogrzewanie: WŁĄCZONE"), print("Powód: temperatura poniżej 20°C i ktoś jest w domu")
        else:
            print("Ogrzewanie: WYŁĄCZONE"), print("Powód: temperatura nie jest niższa niż 20°C")
    else:
        if float(temperatura) < 16:
            print("Ogrzewanie: WŁĄCZONE"), print("Powód: temperatura poniżej 16°C i nikogo nie ma w domu")
        else:
            print("Ogrzewanie: WYŁĄCZONE"), print("Powód: temperatura nie jest niższa niż 16°C i nikogo nie ma w domu")