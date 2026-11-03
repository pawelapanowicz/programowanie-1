import matplotlib.pyplot as plt

ile = int(input("Podaj liczbe studentow: "))
nazwiska = []
punkty = []
oceny = []
for i in range(ile):
    nazwisko = input(f"Nazwisko studenta {i+1}: ")
    pkt = int(input("Punkty: "))
    if pkt >= 90:
        ocena = 5.0
    elif pkt >= 80:
        ocena = 4.5
    elif pkt >= 70:
        ocena = 4.0
    elif pkt >= 60:
        ocena = 3.5
    elif pkt >= 50:
        ocena = 3.0
    else:
        ocena = 2.0
    nazwiska.append(nazwisko)
    punkty.append(pkt)
    oceny.append(ocena)
for nazwisko, ocena in zip(nazwiska, oceny):
    print(nazwisko, "-", ocena)
print("Srednia ocen:", sum(oceny) / len(oceny))
print("Liczba zaliczen:", sum(1 for ocena in oceny if ocena >= 3.0))
print("Generowanie wykresu...")
plt.bar(nazwiska, oceny)
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.grid(axis="y", alpha=0.3)
plt.savefig("oceny.png")
plt.show()