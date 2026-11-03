ile = int(input("Podaj liczbe pomiarow: "))
pomiary = []
for i in range(ile):
    pomiar = int(input(f"Pomiar {i+1}: "))
    pomiary.append(pomiar)
prog = 50
alarmowe = [x for x in pomiary if x > prog]
podwojone = [x * 2 for x in pomiary]
print("Pomiary alarmowe:", alarmowe)
print("Pomiary pomnozone przez 2:", podwojone)
if any(x > prog for x in pomiary):
    print("Czy wystapil alarm? Tak")
else:
    print("Czy wystapil alarm? Nie")
if all(x <= prog for x in pomiary):
    print("Czy wszystkie pomiary sa prawidlowe? Tak")
else:
    print("Czy wszystkie pomiary sa prawidlowe? Nie")