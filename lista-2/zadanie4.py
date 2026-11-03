temperatury = []
for i in range(7):
    temp = float(input(f"Dzien {i+1}: "))
    temperatury.append(temp)
    srednia = sum(temperatury) / len(temperatury)
print("Średnia:", srednia, "C")
najwyzsza = max(temperatury)
print("Najwyższa:", najwyzsza, "C")
najniższa = min(temperatury)
print("Najniższa:", najniższa, "C")
powyzej_sredniej = sum(1 for temp in temperatury if temp > srednia)
print("Powyżej średniej:", [i+1 for i, temp in enumerate(temperatury) if temp > srednia])
print("Liczba dni:", powyzej_sredniej)
