wiek = input("Podaj wiek: ")
zgoda = input("Czy masz zgodę opiekuna?: ")
dokument = input("Czy masz dokument tożsamości?: ")
if int(wiek) >= 18 and dokument.lower() == "tak":
    print("Wypozyczenie mozliwe.")
elif int(wiek) < 18 and int(wiek) >= 13 and zgoda.lower() == "tak" and dokument.lower() == "tak":
    print("Wypozyczenie mozliwe.")
else:
    print("Wypozyczenie niemozliwe.")