cena_produktu = input("Podaj cenę produktu: ")
rabat = input("Podaj rabat w procentach: ")
wartosc_produktu = float(cena_produktu) * (1 - float(rabat) / 100)
print("Cena początkowa:", cena_produktu, "zł")
print("Kwota rabatu:", float(cena_produktu) * float(rabat) / 100, "zł")
print("Cena po rabacie:", wartosc_produktu, "zł")
if int(rabat) >= 20:
    print("Duża promocja!")
else:
    print("Standardowa promocja.")
