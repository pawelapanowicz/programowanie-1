ile = int(input("Ile pomiarow chcesz wprowadzic? "))
pomiary = []
for i in range(ile):
    pomiar = int(input(f"Pomiar {i+1}: "))
    pomiary.append(pomiar)
print("Pierwszy pomiar:", pomiary[0])
print("Ostatni pomiar:", pomiary[-1])
print("Pierwsze trzy:", pomiary[:3])
print("Ostatnie trzy:", pomiary[-3:])
print("Co drugi pomiar:", pomiary[::2])
print("Odwrocona lista:", pomiary[::-1])
kopia = pomiary.copy()
kopia[0] = 0
print("Oryginal:", pomiary)
print("Kopia po zmianie:", kopia)