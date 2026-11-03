produkty = []
ceny = []
ile = int(input("Podaj liczbe produktow: "))
for i in range(ile):
    produkt = input(f"Produkt {i+1}: ")
    cena = int(input("Cena: "))
    produkty.append(produkt)
    ceny.append(cena)
print("=== CENNIK ===")
for numer, (produkt, cena) in enumerate(zip(produkty, ceny), start=1):
    print(f"{numer}. {produkt} - {cena} zl")
print("Suma cen:", sum(ceny), "zl")
najdrozszy = max(ceny)
print("Najdrozszy produkt:", produkty[ceny.index(najdrozszy)], "-", najdrozszy, "zl")